def get_info(city, country, population=None):
    """this func prints whole info about place at once"""
    msg = (str(city).title() + ', ' + str(country).title())
    if population:
        msg += ', ' + str(population)
    return msg