/**
 * Definition for singly-linked list.
 * */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;
  //   this will calculate gcd
  function gcd({ big, small }: { big: number; small: number }): number {
    let gcd = 0;
    while (small != 0) {
      let rem = big % small;
      gcd = small;
      big = small;
      small = rem;
    }
    return gcd;
  }

  let current = head;
  while (current && current.next) {
    let big = Math.max(current.val, current.next.val);
    let small = Math.min(current.val, current.next.val);
    
    let nodeVal = gcd({ big, small });
    // Create new node with GCD value, pointing to the next node
    let newNode = new ListNode(nodeVal, current.next);
    // Insert the new node between current and current.next
    current.next = newNode;
    // Move to the node after the newly inserted node
    current = newNode.next!;
    
  }

  return head;
}
