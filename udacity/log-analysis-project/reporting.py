'''
Logs Analysis Project.

Please note that this code will work only if database views were created.
Views are described in Readme.md.
'''
import psycopg2


def popular_articles():
    '''
    This function returns TOP 3 popular articles.
    '''
    datb = psycopg2.connect(database='news')
    conn = datb.cursor()
    conn.execute("select * from title_views;")
    result = conn.fetchall()
    for output in result:
        print "%s | %s" % (output[0], output[1])
    conn.close()


def popular_authors():
    '''
    This function returns all popular authors.
    '''
    datb = psycopg2.connect(database='news')
    conn = datb.cursor()
    conn.execute("select * from  author_count;")
    result = conn.fetchall()
    for output in result:
        print "%s | %s total views" % (output[0], output[1])
    conn.close()


def log_errors():
    '''
    This function returns all errors waht were returned on different days.
    '''
    datb = psycopg2.connect(database='news')
    conn = datb.cursor()
    conn.execute("""select date, round((100* sum / (SUM(sum) OVER ())),1) "% of errors", status from error_log2;""")
    result = conn.fetchall()
    for output in result:
        print "On the %s were %s%% requests lead to errors" % (output[0], output[1])
    conn.close()


print "Three most popular articles are:" + '\n'
popular_articles()
print '\n' + "The most popular authors are:" + '\n'
popular_authors()
print '\n' + "Days when requests lead to errors:" + '\n'
log_errors()