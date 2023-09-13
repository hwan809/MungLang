from compiler import MungLanguage as Interpreter
from os import remove as rm
from traceback import print_exc as error_log

'''
suggest by 향동중학교 30319 이인환
dev on SAMSUNG S20 - Termux.apk [vim]

comment : 아직 뭉탱이 밈 잘 몰라여
comment : 학교에서 아는 친구가 안죄송하다 밈의 캐인맨을 알려줘서 뭉탱이 영상 재미있게 보고 있습니다.

debug at 9:40 on 2023.9.13
'''

class ShellEnd(Exception): pass

def pickleable_munglang_w(f):
    return open(f, 'w', encoding='utf-8-sig')

def with_opener(opener):
    def with_decorater(func):
        def with_wrapper_processor(file):
            with opener(file) as fp:
                return func(fp)
        return with_wrapper_processor
    return with_decorater

@with_opener(pickleable_munglang_w)
def temp_make_process(fp):
    a = input('>>> ')
    fp.write(a + '\n')
    active = False
    if a == '안죄송하다!':
        return ShellEnd("shell is broked by kain lol (케인님이 쉘을 부쉈습니닼ㅋㅋㅋ)")
    ret = False
    while a != "!춘잣":
        if active:
            fp.write(a + '\n')
        else:
            active = True
        a = input('... ')
        ret = True
    return ret

def exec_lines(interpreter = Interpreter):
    src = 'temp.mte'
    temp_interpreter = interpreter()
    end_condition = temp_make_process(src)
    if not type(end_condition) is bool:
        raise end_condition
    elif end_condition:
        temp_interpreter.compile_file(src)
    rm(src)

def shell(last_interrupt = True):
    print("뭉랭 쉘이다 임마!")
    print('"!춘잣"으로 입력 완료란다. 얘. (쉘 한정이란다.)')
    print('입력소스는 실시간 유출 가능하단다. 얘, (temp.mte에 저장된단다. 얘.)')
    print('"안죄송하다!"로 쉘 종료란다.  (당연히 쉘 한정이란다.)')

    do = False

    while 1:
        try:
            exec_lines()
        except ShellEnd as end_log:
            print(end_log)
            error_log()
            do = True
            break
        except Exception as error:
            print(type(error), ':', error)
            error_log()
    if do:
        rm('temp.mte')
    if last_interrupt:
        input('[ENTER -> 종료]')

if __name__ == "__main__": shell()
