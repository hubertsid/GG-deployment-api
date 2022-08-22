import sqlite3

def give_reccomendations(games):
    choices = []
    titles = []
    ar = []
    tag_premium = []

    choices = games
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    for choice in choices:
        query = "SELECT * FROM games WHERE title = ?"
        ch = [choice]
        c.execute(query,(ch))
        results = c.fetchall()
        for res in results[0][3:7]:
            tag_premium.append(res)


    for choice in choices:
        tags = []
        query = "SELECT * FROM games WHERE title = ?"
        ch = [choice]
        c.execute(query,(ch))
        results = c.fetchall()

        for res in results[0][3:7]:
            tags.append(res)
        
        for res in results[0][8:12]:
            titles.append(res)
            titles.append(res)

        for tag in tags:
            # tag repetition premium
            premium = tag_premium.count(tag)*0.1


            tg = tag.replace(" ", "_")
            query = "SELECT * FROM `{}`".format(tg)
            t = [tg]
            c.execute(query)
            results = c.fetchall()

            for result in results:
                titles.append(result[1])

            for i in titles:
                record = (titles.count(i)+premium,i)
                if record in ar or i in choices:
                    continue
                ar.append(record)

    ar.sort()
    n = ar.count(())
    ar.reverse()
    reccomendations = []
    cq = 0
    for i in ar:
        if i[1] not in reccomendations:
            reccomendations.append(i[1])
            cq+=1
        if cq==20:
            break

    return reccomendations