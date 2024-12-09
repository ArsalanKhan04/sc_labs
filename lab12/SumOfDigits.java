import java.util.List;
import java.util.ArrayList;


public class SumOfDigits {
  private static int SumOfDigits(int num){
    if (num == 0)
      return 0;
    if (num < 0) num *= -1;
    int num_divide = num / 10;
    int num_mod = num % 10;
    return (SumOfDigits(num_divide) + num_mod);
  }
  public static void main(String[] args) {
    System.out.println(SumOfDigits(567));
  }
}
