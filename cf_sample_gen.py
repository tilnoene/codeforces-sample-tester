import requests
from bs4 import BeautifulSoup as bs

def remove_first_line(text):
    temp = text.split('\n', 1)[1]

    if temp[-1] == '\n':
        return temp
    
    return temp + '\n'

def save_sample(problem, samples):
    input_samples = samples.find_all('div', class_='input')
    output_samples = samples.find_all('div', class_='output')
    
    for i in range(len(input_samples)):
        archive = open(f'{problem}_input{i+1}.txt', 'w')
        input_curr = remove_first_line(input_samples[i].text)
        archive.write(input_curr)
        archive.close()

        archive = open(f'{problem}_output{i+1}.txt', 'w')
        output_curr = remove_first_line(output_samples[i].text)
        archive.write(output_curr)
        archive.close()

def get_problem_item(index):
    return chr(index+65)

def cf_sample_gen(url):
    r = requests.get(url).text

    soup = bs(r, 'html.parser')
    samples = soup.find_all('div', class_='sample-test')

    for i in range(len(samples)):
        save_sample(get_problem_item(i), samples[i])

# example_input: 1536
# for link: https://codeforces.com/contest/1536/problems
cf_sample_gen(f'https://codeforces.com/contest/{input()}/problems')