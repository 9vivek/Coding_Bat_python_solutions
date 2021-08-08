def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:    
    return True
  if not a_smile and not b_smile :
    return True
  else:
    return False
    
    
def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  else:
    return a+b



def diff21(n):
  if n>21:
    return 2*(n-21)
  else:
    return abs(n-21)

def parrot_trouble(talking, hour):
  if (hour<7 or hour>20) and talking :
    return True
  else:
    return False
    
def makes10(a, b):
  if a==10 or b==10:
    return True
  if a+b==10:
    return True
  else:
    return False
    
    
def near_hundred(n):
  if abs(n-100)<=10:
    return True
  if abs(n-200)<=10:
    return True
  else:
    return False



def pos_neg(a, b, negative):
  if negative ==True:
    if a<0 and b<0:
      return True
    else:
      return False
  if a<0 and b>0:
    return True
  if a>0 and b<0:
    return True
  else:
    return False


def not_string(str):
  if len(str)>=3 and str[:3]=='not':
    return str
  else:
    return  'not ' + str

  
  
def missing_char(str, n):
  return str[:n] + str[n+1:]
