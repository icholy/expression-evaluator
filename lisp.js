var tokenize = function (src) {
  var tokens = src.
      replace(/\)/g, " ) ").
      replace(/\(/g, " ( ").
      split(" ");
  var isntEmpty = function (s) { return s != ''; };
  return tokens.filter(isntEmpty);
};
 
var atom = function (x) {
  var i = parseInt(x);
  if (!isNaN(i)) return i;
  var f = parseFloat(x);
  if (!isNaN(f)) return f;
  return x;
};
 
var read = function (tokens) {
  var i;
  var token = tokens.shift();
  if (token === '(') {
    var L = [];
    while (tokens[0] !== ')') {
      L.push(read(tokens));
    }
    tokens.shift()
    return L;
  } else {
    return atom(token);
  }
};
 
var isArray = function (x) {
  return {}.toString.call(x) === '[object Array]'; 
};
 
var add = function (args) {
  if (args.length === 1) {
    return args[0];
  } else {
    return args[0] + add(args.slice(1));
  }
};
 
var multiply = function (args) {
  if (args.length === 1) {
    return args[0];
  } else {
    return args[0] * multiply(args.slice(1));
  }
};
 
var eval = function (ast) {
  if (!isArray(ast)) {
    return ast;  
  } 
  if (ast.length === 0) {
    return null;
  }
  var args = ast.slice(1).map(eval);
  switch (ast[0]) {
  case '+': return add(args);
  case '*': return multiply(args);
  default:
    throw new Error("invalid function call!");
  }
};
 
var src = "(+ (* 1 4) (+ 5 3))";
 
console.log(eval(read(tokenize(src))));
