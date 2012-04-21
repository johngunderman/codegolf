import sys

class DocumentIndex(object):

    def __init__(self, f):
        self._file = f
        self._dict = dict()
        self._keys = list()

        for line in self._file:
            kv = line.split(" : ")
            if len(kv) != 2:
                continue

            index = kv[0]
            review = kv[1]

            words = review.split(" ")

            for word in words:
                for i in range(0,len(word)):
                    subword = word[i:]
                    if subword in self._dict:
                        bucket = self._dict[subword]
                        bucket.append(index)
                    else:
                        bucket = [index]
                        self._dict[subword] = bucket

        self._keys = self._dict.keys()
        self._keys.sort()

    def query(self, query_str):
        hi = len(self._keys) - 1
        lo = 0

        qs = query_str.split(' ')
        results = list()

        for q in qs:
            while (lo <= hi):
                mid = int((lo + hi) / 2)
                res = self.cmp_str(self._keys[mid], q)

                if (res < 0):
                    lo = mid + 1
                elif (res > 0):
                    hi = mid - 1
                else:
                    results.append(self.matching(mid, q))
                    break

        if len(results) > 0:
            res = results[0]
            for r in results:
                res = set(res) & set(r)
            return list(res)
        else:
            return []


    def cmp_str(self, key, query_str):
        try:
            for x in range(0, len(query_str)):
                if key[x] > query_str[x]:
                    return 1
                if key[x] < query_str[x]:
                    return -1
            return 0
        except IndexError:
            return 1


    def matching(self, mid, query_str):
        results = []
        key = self._keys[mid]
        m = mid

        while (self.cmp_str(key, query_str) == 0):
            results.extend(self._dict[key])
            m -= 1
            key = self._keys[m]

        m = mid + 1
        while(self.cmp_str(key, query_str) == 0):
            results.extend(self._dict[key])
            m += 1
            key = self._keys[m]

        return results

if __name__ == "__main__":
    filename = sys.argv[1]
    f = open(filename, "r")
    di = DocumentIndex(f)

    while True:
        inp = raw_input("> ")
        results = di.query(inp)
        print results

