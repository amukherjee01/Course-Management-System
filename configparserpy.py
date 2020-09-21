from configparser import ConfigParser


def getcreds(file="dbconfig.ini", section="mysql"):

    dbdict = {}

    parser = ConfigParser()

    parser.read(file)

    if parser.has_section(section):
        items = parser.items(section)
        print(items)
        for item in items:
            dbdict[item[0]] = item[1]
    print(dbdict)
    return dbdict


getcreds()
