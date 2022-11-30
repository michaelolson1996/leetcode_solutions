class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        highest_amount = 0
        current_amount = 0

        for customer in accounts:
            for bank in customer:
                current_amount = current_amount + bank
            if current_amount > highest_amount:
                highest_amount = current_amount
            current_amount = 0
        
        return highest_amount

