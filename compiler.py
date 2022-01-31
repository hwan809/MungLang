import sys

TYPE_IF = 'IF'
TYPE_DEF = 'DEF'
TYPE_CALL = 'CALL'
TYPE_INPUT = 'INPUT'
TYPE_PRINT = 'PRINT'
TYPE_GOTO = 'GOTO'
TYPE_END = 'END'
TYPE_BLANK = 'BLANK'


class MungLanguage:
    def __init__(self):
        self.index = 0
        self.data = [0] * 256

    def get_int(self, code):
        plus = code.count('.')
        minus = code.count('~')

        code = code.replace('.', '')
        code = code.replace('~', '')

        if not code.empty():
            raise SyntaxError(f'얘! {self.index + 2}번째 줄에 이것 좀 보렴. 이게 니 눈에 정수처럼 보이냐?')

        return plus - minus

    def get_number(self, code):
        output = 0
        now_add = True

        while len(code) != 0:
            if code.startswith('자~'):
                if now_add:
                    output += int(input())
                else:
                    output *= int(input())
                    now_add = True

                code = code.split('~', maxsplit=1)[1]
            elif code.startswith('탱'):
                if now_add:
                    output += self.data[0]
                else:
                    output *= self.data[0]
                    now_add = True

                code = code[1:]
                # print(f'{self.index + 2} line, {code}')
            elif code.startswith('태'):
                now_call = code.split('앵')[0] + '앵'

                now_num = self.get_variable(now_call)
                if now_add:
                    output += now_num
                else:
                    output *= now_num
                    now_add = True

                # print(code)
                code = code[len(now_call):]
            elif code.startswith('.') or code.startswith('~'):
                now_char = code[0]
                now_num = 0

                while now_char == '.' or now_char == '~':
                    if not code:
                        break

                    now_char = code[0]

                    if now_char == '.':
                        now_num += 1
                    elif now_char == '~':
                        now_num -= 1
                    else:
                        break

                    code = code[1:]

                if now_add:
                    output += now_num
                else:
                    output *= now_num
                    now_add = True
            elif code.startswith('코'):
                now_add = False
                code = code[1:]

        return output

    def get_variable(self, code):
        index = -1

        if code == '탱':
            index = 0
        elif code == '태앵':
            index = 1

        else:
            if code[0] == '태' \
                    and code[-1] == '앵':
                for char in code[1:-1]:
                    if char != '애':
                        raise SyntaxError(f'얘! index {self.index + 2} 줄에 이게 변수 호출이 되겠니?')

                index = len(code) - 1
            else:
                raise SyntaxError(f'얘! index {self.index + 2} 줄에 이게 변수 호출이 되겠니?')

        return self.data[index]

    def variable_index_to_number(self, code):
        if code == '뭉':
            return 0
        elif code == '무웅':
            return 1
        else:
            if code[0] == '무' \
                    and code[-1] == '웅':

                for char in code[1:-1]:
                    if char != '우':
                        raise SyntaxError(f'얘! {self.index + 2}번째 줄에 이게 변수 인덱스가 되겠니?')

                return len(code) - 1

            else:
                raise SyntaxError(f'얘! {self.index + 2}번쨰 줄에 이게 변수 인덱스가 되겠니?')

    @staticmethod
    def get_type(self, code):
        if not code:
            return TYPE_BLANK
        elif code.startswith('무빙'):  # GOTO문 무빙
            return TYPE_GOTO
        elif code.startswith('유링계숭한?'):  # IF문 유링계숭한
            return TYPE_IF
        elif code.startswith('뭉') or code.startswith('무'):  # 변수 선언 뭉
            return TYPE_DEF
        elif code.startswith('자'):  # 변수 출력/입력 자!/자~
            return TYPE_PRINT
        elif code.startswith('아이그냥'):  # RETURN문 아이그냥
            return TYPE_END
        else:
            raise SyntaxError(f'얘! {self.index + 2}번째 줄 이게 무슨 구문이니! 음.. 죽여벌랑')

    def compileLine(self, code):
        if code == '':
            return None

        TYPE = self.get_type(self, code)

        if TYPE == TYPE_BLANK:
            return

        if TYPE == TYPE_DEF:
            # 예시: 무우웅~~
            var_index, number_str = -1, -1
            if (code.startswith('뭉')):
                var_index = 0
                number_str = code[1:]
            else:
                var_index, number_str = code.split('웅', maxsplit=1)
                var_index += '웅'
                var_index = self.variable_index_to_number(var_index)

            number_int = self.get_number(number_str)
            self.data[var_index] = number_int

            # print('data added in index ' + str(var_index) + '. value : ' + str(number_int))
        elif TYPE == TYPE_PRINT:

            number = code
            if number[-1] == '!':
                number = number[1:-1]
            else:
                raise SyntaxError(f'얘! {self.index + 2}번째 줄에 지금 그걸 출력하겠다고 하는 거니?')

            if not number or number == '0':
                print('\n', end='')
            else:
                # print(f'{self.index} line, {number}')
                number_int = self.get_number(number)
                if number_int > 0:
                    number_ascii = chr(number_int)
                    print(number_ascii, end='')
                else:
                    print(-number_int, end='')
        elif TYPE == TYPE_END:
            number = code[4:]
            number_int = self.get_number(number)

            print(number_int, end='')
            # self.index = self.
        elif TYPE == TYPE_IF:
            command = code[6:]  # 유링계숭한? 후.

            check_val, wish = command.split(',', maxsplit=1)
            check_val_int = self.get_number(check_val)

            if check_val_int == -3000:
                return wish
        elif TYPE == TYPE_GOTO:
            number = code[2:]
            number_int = self.get_number(number)

            return number_int - 2

    def compile(self, code):
        self.index = 0

        if code[0] != '춘잣!':
            raise SyntaxError('얘! 뭉탱어는 춘잣! 아니면 겸상 안한단다? 개발이 잘 안되니?')

        del code[0]
        now_moving = False

        while self.index < len(code):
            # print(f'compiling line {self.index + 2}... {code[self.index]}')

            goto = self.compileLine(code[self.index])
            self.index += 1

            if isinstance(goto, int):
                if now_moving:
                    now_moving = False
                    del code[self.index - 1]
                    # print(f'moving to, {code[self.index]}')

                self.index = goto
            elif isinstance(goto, str):
                code.insert(self.index, goto)
                now_moving = True
                # print(now_moving)

    def compile_file(self, path):
        with open(path, encoding='utf-8-sig') as mte_file:
            code = mte_file.read().splitlines()
            self.compile(code)


if __name__ == '__main__':
    compiler = MungLanguage()
    compiler.compile_file('munglangtest.mte')
