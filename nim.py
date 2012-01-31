class Nim(object):
    def __init__(self):
        self.players = ['Player 1', 'Player 2']
        self.board   = [1, 2, 3, 4, 5]
    
    def play(self):
        while True:
            for player in self.players:
                self.take_turn(player)
                if sum(self.board) == 0:
                    print player + ' won!'
                    return
    
    def take_turn(self, player):
        print player + '\'s Turn:'
        self.display_board()
        row   = self.get_row()
        count = self.get_int('How many stars? ', 1, self.board[row - 1])
        self.board[row - 1] = self.board[row - 1] - count
    
    def get_row(self):
        answer = None
        while answer is None:
            row  = self.get_int('Which row? ', 1, len(self.board))
            if self.board[row - 1] == 0:
                print 'That row is empty!'
            else:
                answer = row
        return answer
    
    def get_int(self, prompt, min_value, max_value):
        answer = None
        while answer is None:
            response = raw_input(prompt)
            try:
                converted = int(response)
                if converted < min_value:
                    print 'That number is too small.'
                elif converted > max_value:
                    print 'That number is too big.'
                else:
                    answer = converted
            except ValueError:
                print 'That is not a number!'
        return answer
    
    def display_board(self):
        for i in range(len(self.board), 0, -1):
            print str(i) + ' : ' + ('*' * self.board[i - 1])

if __name__ == '__main__':
    Nim().play()
