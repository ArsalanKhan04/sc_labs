import java.util.List;
import java.util.ArrayList;


public class Parser {
  public static int multiply(String expression){
    int num1 = expression.charAt(0) - '0';
    if (expression.length() == 1)
      return num1;
    char oper = expression.charAt(1);
    if (oper == '*'){
      return num1 * multiply(expression.substring(2, expression.length()));
    } else {
      return num1 / multiply(expression.substring(2, expression.length()));
    }
  }
  public static int addition(String expression){
    if (expression.length() == 1){
      int num1 = expression.charAt(0) - '0';
      return num1;
    }
    int x = 0;
    while (x < expression.length() && (expression.charAt(x) != '+' && expression.charAt(x) != '-')){
      x++;
    }
    if (x == expression.length()){
      return multiply(expression);
    }
    if (expression.charAt(x) == '+'){
      return addition(expression.substring(0, x))
        + addition(expression.substring(x + 1, expression.length()));
    } else {
      System.out.println(addition(expression.substring(0, x)));
      System.out.println(addition(expression.substring(x + 1, expression.length())));
      return addition(expression.substring(0, x))
        - addition(expression.substring(x + 1, expression.length()));
    }
  }
  public static int evaluateExpression(String expression){
    expression = expression.replaceAll("\\s+", "");
    return addition(expression);
  }
  public static void main(String[] args) {
    System.out.println(evaluateExpression("5*3-2+7"));
  }
}
