## How to use

### ⚙️ Generating samples
First, it is necessary to generate the files containing the samples, to do this, just run:

`cf_sample_gen.sh contest_id` on Ubuntu<br />
`dash cf_sample_gen.sh contest_id` on WSL

```
Example:
contest link: https://codeforces.com/contest/1536`
contest_id: 1536

>>> dash cf_sample_gen.sh 1536
```

**⚠️ You need to install python and bs4 to run this**
```
sudo apt-get install python3 python3-pip
pip3 install bs4
```

### 🛠 Running the samples
Save the archive like `problem.cpp` and run:

`runsamples.sh problem` on Ubuntu<br />
`dash runsamples.sh problem` on WSL

```
Example:
problem: A
archive: A.cpp

>>> dash cf_sample_gen.sh A
```

## Shorten commands
Run in your terminal `alias custom_command='original_command'`. Examples:

```
alias runsamples='dash runsamples.sh'

>>> runsamples A
```
```
alias cf_sample_gen='dash cf_sample_gen.sh'

>>> cf_sample_gen 1536
```

**Contributions are welcome ^^**
- Measure code execution time
- Measure memory consumption of code
- Friendlier error interface when testing samples