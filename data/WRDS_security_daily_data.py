import wrds


class WRDSDataScraper:
    """
    Wharton Research Data Services data retrieval to analyze models. We hope to use a variety of data sources
    provided in the
    """

    def __init__(self):
        self.conn = wrds.Connection()

    def retrieve_data(self, library: str, table: str, *obs):
        """
        General method to retrieve data from WRDS database

        :param library: name of the libary in WRDS
        :param table: name of the table in WRDS
        :param obs: number of observations to pass
        :return:
        """

        return self.conn(library=library, table=table)
