import sys

class DocumentIndex(object):
    """Acts as an index for the data given upon object instantiation
    """

    def __init__(self, f):
        """Initializes the index with the contents of 'f'
        """
        self._file = f

    def query(self, query_str):
        """Returns a list of records matching the query string for
        this index.
        """
        pass



if __name__ == "__main__":
    filename = sys.argv[1]
    f = open(filename, "r")
    di = DocumentIndex(f)

    # start our input loop:
    while True:
        try:
            inp = raw_input(">")
            results = di.query(query_str)
            print results
        except:
            break
