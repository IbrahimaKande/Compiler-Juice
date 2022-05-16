reserved = {
    'var': 'VAR',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'input': 'INPUT',
    'output': 'OUTPUT',
    'function': 'FUNCTION'
}

tokens = ['EQUAL', 'CONST', 'IDENT'] + list(reserved.values())

t_EQUAL = r'=='
literals = ['.', ';', '{', '}', '(', ')', '=', '+', '-', '<', '>', ',']

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_CONST(token):
    r'[0-9][0-9]*'
    token.value = int(token.value)
    return token

def t_NEWLINE(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_error(token):
    message = 'Unknown token:'
    message = '\nType: ' + token.type
    message += '\nValue: ' + str(token.value)
    message += '\nLine: ' + str(token.lineno)
    message += '\nPosition: ' + str(token.lexpos)
    raise Exception(message)