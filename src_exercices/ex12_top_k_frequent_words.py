class Solution(object):

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]

        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4
        Output: ["the","is","sunny","day"]

        """
        ''
        dic_words_count = {}

        for w in words:
            if w in dic_words_count.keys():
                dic_words_count[w] += 1
            else:
                dic_words_count[w] = 1

        if k == 0:
            return []
        else:
            dic_words_count_ordered = dict(sorted(dic_words_count.items(), key=lambda item: (-item[-1], item[0])))

        k_max = min(len(dic_words_count_ordered), k)
        ret = [''] * k_max
        k_idx = 0
        for key in dic_words_count_ordered.keys():
            if k_idx == k_max:
                break
            ret[k_idx] = key
            k_idx += 1

        return ret
