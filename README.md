
## Password Generator

This is a simple Python script that generates a random password of a given length using the `random` and `string` modules.

### How it works

The `genrate_password` function takes a single argument `length`, which specifies the length of the password to be generated. It generates a password consisting of a combination of uppercase and lowercase letters, digits, and punctuation characters using the `string.ascii_letters`, `string.digits`, and `string.punctuation` constants.

The function then loops through the specified length of the password, using the `random.choice` function to randomly select a character from the list of available characters for each position of the password.

Finally, the function returns the generated password as a string.

### Usage

To use the script, simply run it from the command line and enter the desired length of the password when prompted. The script will then generate a random password of the specified length and print it to the console.

For example:

```
Enter the length of the Password: 12
Generated Password:  #h&$IVx7W8}C
```
