zoo = ('lion', 'tiger', 'cat', 'dog', 'monkey', 'cat')
print(f'zoo: {zoo}')
print(zoo[2]) # 인덱싱
print(zoo[1:]) # 슬라이싱
print('lion' in zoo) # 멤버십 테스트
#수정 불가하므로 에러 발생
# zoo[3] = 'spider' 
print(f"zoo.index('tiger'): {zoo.index('tiger')}")
print(f"zoo.count('cat'): {zoo.count('cat')}")