import java.util.List;
import java.util.ArrayList;


public class BinarySearch {
  public static int binarySearch(int[] arr, int left, int right, int target) {
    if (left > right) {
      return -1;
    }
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) {
      return mid + 1;
    } else if (arr[mid] < target) {
      return binarySearch(arr, mid + 1, right, target);
    } else {
      return binarySearch(arr, left, mid - 1, target);
    } 
  }
  public static int binarySearchString(String[] arr, int left, int right, String target){
    if (left > right) {
      return -1;
    }
    int mid = left + (right - left) / 2;
    int comps = arr[mid].compareTo(target);
    if (comps == 0) {
      return mid + 1;
    } else if (comps < 0) {
      return binarySearchString(arr, mid + 1, right, target);
    } else {
      return binarySearchString(arr, left, mid - 1, target);
    } 
  }
  public static ArrayList<Integer> binarySearchAll(int[] arr, int left, int right, int target){
    int ind = binarySearch(arr, left, right, target);
    int lft = ind;
    int rgt = ind;
    ArrayList<Integer> sol = new ArrayList<>();
    if (ind == -1)
      return sol;
    while (lft >= left && arr[lft] == target)
      lft--;
    while (rgt < right && arr[rgt] == target)
      rgt++;
    for (int i = lft + 1; i < rgt; i++){
      sol.add(i + 1);
    }
    return sol;
  }
  public static void main(String[] args) {
    int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    String[] arr2 = {"aaaaa", "abbbb", "acccc"};
    int target = 5;
    int result = binarySearch(arr, 0, arr.length - 1, target);
    System.out.println(result);
    result = binarySearchString(arr2, 0, arr2.length-1, "ball");
    System.out.println(result);
    int[] arr3 = {1, 1, 2, 2, 2, 2, 2, 2, 3, 3};
    ArrayList<Integer> result2 = binarySearchAll(arr3, 0, arr3.length-1, 2);
    System.out.println(result2);

  }
}
