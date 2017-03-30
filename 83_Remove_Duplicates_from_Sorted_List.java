"""
Author:     Wang, Fangyijie
Date:       Mar 30, 2017
Problem:    Remove Duplicates from Sorted List
Difficulty: Easy
Source:     https://leetcode.com/problems/remove-duplicates-from-sorted-list/#/description
Descriptions:
    Given a sorted linked list, delete all duplicates such that each element appear only once.
Example:
    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.
"""

public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }
        ListNode temp = head;
            
        while(temp != null && temp.next != null) {
            if(temp.val == temp.next.val) {
                temp.next = temp.next.next;
            }else {
                temp = temp.next;
            }
        }
        return head;
    }
}