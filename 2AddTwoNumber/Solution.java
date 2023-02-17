/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;
class Solution {
  public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int l1Num = 0;
    int l2Num = 0;
    
    while(l1 != null){
      l1Num = l1Num*10 + l1.val;
      l1 = l1.next;
    }  
    //System.out.println(l1Num);
    while(l2 != null){
      l2Num = l2Num*10 + l2.val;
      l2 = l2.next;
    }
    // System.out.println(l2Num);
    
    //extract num
    int num = l1Num + l2Num;
    //if only digit is 0, return 0
    if(num == 0)return new ListNode(0);
    
    System.out.println(num);
    int len = String.valueOf(num).length();
    //System.out.println(len);
    //put digits in arr
    int[] arr = new int[len];
    for(int i = 0;i<len;i++){
      arr[i] = num%10;
      num = num/10;
      System.out.println(arr[i]);
    }
    
    //put digits in list
    List<Integer> list = new ArrayList<Integer>(arr.length);
    for (int i : arr)
    {
      list.add(i);
    }
    System.out.println("list "+ list);
    
    //add to ListNode
    ListNode head = new ListNode();
    // System.out.println("head " + head.val);
    
    //
    ListNode node = new ListNode(arr[len-1]);
    System.out.println("head node " + node.val);
    head.next = node;
    if(len==1)return head.next;
    
    
    for(int i=len-2;i>=0; i--){
      node.next = new ListNode(arr[i]);
      node = node.next;
      System.out.println("round "+i+"val "+node.val);
    }
    
    return head.next;
    /*
     int[] ints = {1, 2, 3};
     List<Integer> intList = new ArrayList<Integer>(ints.length);
     for (int i : ints)
     {
     intList.add(i);
     }
     */  
  }
  public static void main(String[] args){
    ListNode l1 = new ListNode(3);
    l1.next = new ListNode(4);
    l1.next.next = new ListNode(2);
    
    ListNode l2 = new ListNode(4);
    l2.next = new ListNode(6);
    l2.next.next = new ListNode(5);
    
    ListNode l = addTwoNumbers( l1,  l2);
    while(l!=null){
      System.out.print(l.val);
      l=l.next;
    }
  }
}