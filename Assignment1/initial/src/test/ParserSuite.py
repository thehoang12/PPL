import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """procedure main ();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_simple_program_202(self):
        input = """PROCEDURE main (); 
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_wrong_miss_close(self):
        """Miss ) int main( beginend"""
        input = """PRocedure main();
         begin
         a := -12;
         end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_variable_declaration_204(self):
        input = """Procedure main();
        begin
            var x:real;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_variable_declaration_205(self):
        input = """Procedure main();
        begin
            var x:REal;
                y,x,z:Integer;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_variable_declaration_206(self):
        input = """Procedure main();
        begin
            var x:integer;
                tem_:array[1 .. 5] of integer;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_variable_declaration_207(self):
        input = """Procedure main();
        begin
            var x:integer;
                y,x,z:reAl;
                tem_:array[1 .. 5] of real;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_function_declaration_208(self):
        input = """ 
        function abc():integer;
        var a:integer;
        begin
        end
        Procedure main();
        begin

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_function_declaration_209(self):
        input = """ 
        function abc():real;
        var a:integer;
        begin
            a:=5;
            c:=b--5;
        end
        Procedure main();
        begin

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_function_declaration_210(self):
        input = """ 
        function abc():array [1 .. 3] of real;
        var a:integer;
        begin
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_function_declaration_211(self):
        input = """ 
        function abc():array [1 .. 3] of string;
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
            a:=5;
            c:=b-5;
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_procedure_declaration_212(self):
        input = """ 
        Procedure abc();
        var a:integer;
            begin
            end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_procedure_declaration_213(self):
        input = """ 
        Procedure abc();
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_procedure_declaration_214(self):
        input = """ 
        Procedure abc();
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
            a:=5;
            c:=b-5;
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_assignment_stat_215(self):
        input = """ 
        Procedure main();
        begin
            a:= 5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_assignment_stat_216(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= 5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_assignment_stat_217(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()[5];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_assignment_stat_218(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()+dfc();
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    #chu y testcase nay
    def test_assignment_stat_219(self):
        input = """ 
        Procedure main();
        begin
            b:= a < b - c > d /f +g;
            a:= n and 10 and b and 5;
            a:=b:=c:= (abc()+dfc())[1];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_if_stat_220(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
             a:=5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_if_stat_221(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                a:=b;
            else
                b:=a;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_if_stat_222(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
            else
                b:=a;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_if_stat_223(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
                else
                    if a>3 then
                        a:=3;
                    else
                        a:=3;
            else
                b:=a;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_while_stat_224(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while n<10 do
                n:=n*n;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_while_stat_225(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            for foo:= 6 To foo < 10 do 
                a := a*b+3+2*5-1;
            while n<10 do
                n:=n*n;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_while_stat_226(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while ((n<10) and (a>b)) do
                n:=n*n;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_exp_227(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_exp_228(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_exp_229(self):
        input = """ 
        Procedure main();
        begin
            n:= a - b or c and d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_exp_230(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d or e and f and g;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_exp_231(self):
        input = """ 
        Procedure main();
        begin
            n:= 5>=a;
            m:= 6<=5;
            q:= 5<>2;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_exp_232(self):
        input = """ 
        Procedure main();
        begin
            n:= true;
            m:= false;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_exp_233(self):
        input = """ 
        Procedure main();
        begin
            n:= not a;
            m:= a+-c;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_exp_234(self):
        input = """ 
        Procedure main();
        begin
            n:= not (not a);
            n:= not not a;
            m: = - (-c);
            m:= --c;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_exp_235(self):
        input = """ 
        Procedure main();
        begin
            n:= 5--6;
            m:= m+5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_exp_236(self):
        input = """ 
        Procedure main();
        begin
            a:=a+5;
            b:=a-5;
            c:=5/2;
            d:=6*5;
            e:=g mod 5;
            g:=h div 5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_exp_237(self):
        input = """ 
        Procedure main();
        begin
            a:= c/5/5-3+2--2*123+b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_exp_238(self):
        input = """ 
        Procedure main();
        begin
            a:= a and b and not c and d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_exp_239(self):
        input = """ 
        Procedure main();
        begin
            a:= 5+bcd()+edf()[1];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_exp_240(self):
        input = """ 
        Procedure main();
        begin
            n:= a(1,2)[b(123+5)[c(174.145)]];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    # test while for with return ,break and continue
    def test_while_241(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while n<10 do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_while_242(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_while_242(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_while_243(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
                n:=n+1;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_for_244(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=1 to n do
                S:=S*i;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_for_244(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=1 to n do
            begin
                S:=S*i;
                if(S>20) then
                    break;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_for_245(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=n downto i do
            begin
                S:=S*i;
                if(S>20) then
                    break;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_for_246(self):
        input = """ 
        Procedure main();
        begin
            n:=-10;
            S:=1;
            for i:=n downto i do
            begin
                S:=S*i;
                if(S>20) then
                    continue;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_with_247(self):
        input = """ 
        Procedure main();
        begin
            with a:integer;b : array [1 .. 2] of real; do
                b := c[a]+b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_with_248(self):
        input = """ 
        Procedure main();
        begin
            with a:integer;b: array [1 .. 2] of real; do
                begin
                    a:=2;
                    b:= function1();
                end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_call_function_249(self):
        input = """ 
        Procedure main();
        begin
            n:= function1(a,b,c);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_call_function_250(self):
        input = """ 
        Procedure main();
        begin
            while n <2 do begin
                while n>2 do begin
                end
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_call_function_251(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            return n;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))   
    def test_call_function_252(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            return a +1 +3 +5;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252)) 
    def test_call_function_253(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            return func(a);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_call_function_254(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            return func(func());
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_call_function_254(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            return func(func());
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_call_function_255(self):
        input = """ 
        function test() : Integer;
            begin
            n:= function1(function2(),aff[25],c+a);
            return func(func());
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_call_function_256(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            begin
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_call_function_257(self):
        input = """ 
        function test() : Integer;
            n:= function1(function2(),aff[25],c+a);
            begin
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))