import heapq
from collections import defaultdict

# Node 클래스 정의
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq):
    heap = [Node(char, frequency) for char, frequency in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(node, code="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = code
        generate_huffman_codes(node.left, code + "0", code_map)
        generate_huffman_codes(node.right, code + "1", code_map)
    return code_map


def calculate_compression_rate(input_text, encoded_text):
    original_size = len(input_text) * 8  # ASCII는 8비트
    compressed_size = len(encoded_text)
    compression_rate = ((original_size - compressed_size) / original_size) * 100
    return compression_rate


def huffman_encoding():
    # 주어진 문자와 빈도수
    freq = {'k': 10, 'o': 5, 'r': 2, 'e': 15, 'a': 18, 't': 4, 'c': 7, 'h': 11}

    # Huffman 트리 생성
    root = build_huffman_tree(freq)

    # Huffman 코드 생성
    huffman_codes = generate_huffman_codes(root)

    print("Generated Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    # 입력 받기
    while True:
        input_text = input("Please a word: ").strip()
        if not all(char in freq for char in input_text):
            print("illegal character")
        else:
            break

    # 입력된 문장을 Huffman 코드로 인코딩
    encoded_text = ''.join(huffman_codes[char] for char in input_text)

    # 압축률 계산
    compression_rate = calculate_compression_rate(input_text, encoded_text)

    # 결과 출력
    print(f"입력한 텍스트: {input_text}")
    print(f"결과값: {encoded_text}")
    print(f"압축률: {compression_rate:.2f}%")

# 프로그램 실행
huffman_encoding()
