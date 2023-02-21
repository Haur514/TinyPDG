package test001;

public class Test001 {

	int method(A a) {
		if(a == null){
			throw NullPointerException;
		}
		int b = a.num;
		int c = a.num;
		int d = b + c;
		return d;
	}	
}

class A{
	int num;
}
