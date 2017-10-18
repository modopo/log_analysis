# !/usr/bin/env python3

import psycopg2

def connect():
    """Connects to PSQL database. Returns connection if successful"""
    try:
        db = psycopg2.connect(database = "news")
        c = db.cursor()
        return db, c
    except:
        print("Connection unsuccessful!")

def process(query):
    """Performs query and returns result"""
    db, c = connect()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

def get_popular_articles():
    """Prints the top 3 articles of all time"""
    result = process("""select title, count(*) as view 
                            from articles, log 
                                where log.path like '%' || articles.slug || '%'
                                and log.status = '200 OK'
                            group by title 
                            order by view desc 
                            limit 3""")

    print("\n\nThese are the top three articles by views: \n")
    for x in result:
        print('"' + x[0] + '" - ' + str(x[1]))

def get_popular_author():
    """Prints the authors' popularity by page views"""
    result = process("""select authors.name, count(*) as view
                            from articles, authors, log
                                where log.path like '%' || articles.slug || '%'
                                and log.status = '200 OK'
                                and articles.author = authors.id
                            group by authors.name
                            order by view desc""")

    print("\n\nThese are the authors' popularity by views: \n")
    for x in result:
        print(x[0] + " - " + str(x[1]) + " views")

def get_error_rate():
    """Prints the days that have more than 1% error rate"""
    result = process("""select to_char(failed.date, 'Mon DD, YYYY'), failed.fcount, success.scount
                            from (select time::date as date, count(status) as fcount
                                    from log
                                        where status != '200 OK'
                                    group by date) as failed
                            full outer join
                            (select time::date as date, count(status) as scount
                                from log
                                    where status = '200 OK'
                                group by date) as success
                            on failed.date = success.date
                                where fcount * 100 >= (scount + fcount)""")

    print("\n\nThese are the day(s) that have more than 1% of requests lead to error: \n")
    for x in result:
        error = float(x[1])/(float(x[1]) + float(x[2]))
        print(x[0] + ' - ' + str(round(100*error, 2)) + '% error')

get_popular_articles()
get_popular_author()
get_error_rate()


