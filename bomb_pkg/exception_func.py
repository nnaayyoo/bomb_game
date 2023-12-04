# ---------- 예외 함수 ----------
def tw_fo_name(names):
    if (len(names) < 2) or (len(names) > 4) :
        raise ValueError('2-4 명의 이름을 입력해주세요')

def dif_name(names):
    for i in range(len(names)-1) :
        if names[i].replace(' ', '') == names[i+1].replace(' ', '') :
            raise ValueError('이름을 다르게 적어주세요')

def no_empty_name(names):
    for name in names :
        if (name.replace(' ', '') == '') :
            raise ValueError('한 글자 이상의 이름을 입력해주세요')
