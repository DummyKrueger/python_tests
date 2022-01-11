print('Opening test.txt')

with open('./test.txt', 'a') as test_file:
  userInput = input('Write something into test.txt: ') + "\n"
  print('Writing into test.txt...')
  test_file.write(userInput)

print('\n\nReading test.txt...')

with open('./test.txt', 'r') as test_file:
  content = test_file.read()
  print(content)

print('END')