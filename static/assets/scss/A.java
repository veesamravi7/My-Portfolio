class A{
int n1=0,n2=1,n3;
public void fib(int target)
{

System.out.print(n1+" "+n2);
for(int i=2;n3<target;++i)
{
n3=n1+n2;
System.out.print(" "+n3);
n1=n2;
n2=n3;
}
}
public static void main(String args[])
{
A ob=new A();
ob.fib(20);
}
}