/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

class Fraction {
    private int m_num;
    private int m_den;
    
    public void set(int num, int den)
    {
        for (int i = 2; i <= num && i <= den; i++) {
            while (den % i == 0 && num % i == 0) {
                den = den / i;
                num = num / i;
            }
        }
        m_num = num;
        m_den = den;
    }
    
    public String toString()
    {
        return m_num + "/" + m_den;
    }
}

public class Main
{
	public static void main(String[] args) {
	    int numerator = 12;
	    int denominator = 36;
	    
	    Fraction f = new Fraction();
	    System.out.println("Original: " + numerator + "/" + denominator);
	    f.set(numerator, denominator);
	    System.out.println("No common factors: " + f.toString());
	}
}
