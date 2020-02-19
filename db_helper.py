#!/usr/bin/env python3
"""
    Database helper functions.
    Needs sqlite3

"""
def dbdo(dbc, cmd, verbose):
    """
    Execute a database command, optionally printing the cmd if verbose
    """
    if verbose:
        print(cmd)

    result = dbc.execute(cmd)
    return result

def array_from_query(dbc, query_str):
     """
     Return an array from the database.
     only uses the first column returned by the query.
     """
     results = []
     for row in dbc.execute(query_str):
         results.append(row[0])

     return results

def value_from_query(dbc, query_str):
    """
    Return a single value from a query.
    """
    print (query_str)
    results = array_from_query(dbc, query_str)
    if len(results) == 0:
        return 'Null'
    else:
        return results[0]

def dict_from_query(dbc, query_str):
     """
     Return a query as a dict of two elements:
     e.g. select name, rank from staff
     staff['Fred'] = 'Boss'
     Only uses the first two columns of the query.
     """
     results = {}
     for row in dbc.execute(query_str):
         results[row[0]] = row[1]

     return results

def rows_from_query(dbc, query_str):
     """
     Return a list of lists from a database query.
     each list contains a list of all the rows.
     """
     results = []
     for row in dbc.execute(query_str):
         results.append(row)

     return results

def make_tables_from_dict(dbc, tabledefs):
    # Make the Database tables
    print ('Dropping and Building Tables...')
    for table in tabledefs.keys():
        result = dbc.execute('DROP TABLE IF EXISTS [{}]'.format(table))
        result = dbc.execute('CREATE TABLE [{}] ({});'.format(table, tabledefs[table]))