Create Function canUnlockAll
checks whether a list of boxes can be unlocked
If the input boxes is not a list, the function returns False.
If the length of boxes is 0, it also returns False.
Otherwise, it proceeds with further checks.
The function iterates over a range of indices from 1 to len(boxes) - 1.
For each index k, it checks whether k is present in the keys of any box (except the box at index k itself).
If k is found, it breaks out of the inner loop and continues with the next value of k.
If k is not found in any box, it returns False.
If all indices are checked and no issues are found, it returns True.
