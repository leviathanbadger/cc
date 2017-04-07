from syntax.ExprSyntax import *
from syntax.PrimaryExprSyntax import *
from syntax.TermExprSyntax import *
from syntax.Util import isSubclassOfAny

class MultExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, op, rhs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    
    def isHigherPrecedence(self, other):
        return isSubclassOfAny(other, [PrimaryExprSyntax, TermExprSyntax])
    
    def __str__(self):
        return self.precendenceParens(self.lhs) + ' ' + self.op + ' ' + self.precendenceParens(self.rhs)
