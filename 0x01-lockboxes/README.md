# Lockbox

## Here's how the code works

1. We initialize a list called unlocked with False values for each box.
2. We mark the first box as True since it is already unlocked.
3. We create a stack to keep track of boxes we need to visit. We start with the first box (index 0) on the stack.
4. While the stack is not empty, we pop the last box from the stack and check its keys. If a key opens a box that hasn't been unlocked yet, we mark that box as unlocked and add it to the stack.
5. After we have visited all boxes reachable from the starting box, we check if all boxes have been unlocked. If they have, we return True, otherwise we return False.
