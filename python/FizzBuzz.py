class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        i = 0
        fizzbuzz_arr = [None]*n

        while i < n:
            val = i + 1
            if val % 3 == 0 and val % 5 == 0:
                fizzbuzz_arr[i] = "FizzBuzz"
            elif val % 3 == 0:
                fizzbuzz_arr[i] = "Fizz"
            elif val % 5 == 0:
                fizzbuzz_arr[i] = "Buzz"
            else:
                fizzbuzz_arr[i] = str(val)
            i = i + 1

        return fizzbuzz_arr
