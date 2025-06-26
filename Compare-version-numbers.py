def compare_versions(version1: str, version2: str) -> int:
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))

    max_len = max(len(v1_parts), len(v2_parts))
   
    # Compare each part
    for i in range(max_len):
        if v1_parts[i] < v2_parts[i]:
            return -1
        elif v1_parts[i] > v2_parts[i]:
            return 1
    return 0


version1 = input("Enter version 1:")
version2 = input("Enter version 2:")
result = compare_versions(version1, version2)
print("Output: ",result)
