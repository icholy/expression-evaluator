#!/usr/bin/env python
 
Symbol = str
 
def read(sexp):
  return read_form(tokenize(sexp))
 
def tokenize(s):
  return s.replace(')', ' ) ').replace('(', ' ( ').split()
 
def read_form(tokens):
  "Read an expression from the sequence of tokens"
  if len(tokens) == 0:
    raise SyntaxError('unexpected EOF while reading')
  token = tokens.pop(0)
  if token == '(':
    L = []
    while tokens[0] != ')':
      L.append(read_form(tokens))
    tokens.pop(0)
    return L
  elif token == ')':
    raise SyntaxError('unexpected )')
  else:
    return atom(token)
 
def atom(token):
  try: return int(token)
  except ValueError:
    try: return float(token)
    except ValueError:
      return Symbol(token)
 
def eval(x, env):
  if isinstance(x, Symbol):
    return env[x]
  elif not isinstance(x, list):
    return x
  elif len(x) == 0:
    return None
  elif x[0] == 'if':
    if eval(x[1], env):
      return eval(x[2], env)
    else:
      return eval(x[3], env)
  elif x[0] == 'set':
    env[x[1]] = eval(x[2], env)
  else:
    return env[x[0]]([eval(exp, env) for exp in x[1:]])
 
def add(args):
  if len(args) == 1:
    return args[0]
  else:
    return args[0] + add(args[1:])
 
def multiply(args):
  if len(args) == 1:
    return args[0]
  else:
    return args[0] * multiply(args[1:])
 
def subtract(args):
  if len(args) == 1:
    return args[0]
  else:
    return args[0] - add(args[1:])
 
def gt(args):
  return args[0] > args[1]
 
def lt(a, b):
  return args[0] < args[1]
 
def main():
  env = {
      "+"     : add,
      "-"     : subtract,
      "*"     : multiply,
      ">"     : gt,
      "<"     : lt,
      'exit'  : lambda x: exit(0),
      'true'  : True,
      'false' : False,
      'nil'   : None
  }
  while True:
    print ">>>" ,
    print(eval(read(raw_input()), env))
 
if __name__ == "__main__":
  main()
