Sure, I'll add an animated matrix background to the README file. Here's the updated README content:

### Project Name: TOXIC GANG Terminal Script

#### Description:
This project consists of terminal scripts in PHP, Java, Python, and Ruby that display text with highlights and a matrix background color. It also includes basic installation instructions for Termux and the author's Instagram profile.

#### Animated Matrix Background:
```html
<style>
body {
  background-color: black;
}
.matrix {
  font-family: monospace;
  color: lime;
}
</style>
<div class="matrix">
<script>
setInterval(function() {
  let matrix = '';
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  for (let i = 0; i < 150; i++) {
    matrix += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  document.body.innerHTML = matrix;
}, 50);
</script>
```

#### How to Run:
1. **Install Termux:**
   - Install Termux from Google Play Store.

2. **Run the following commands in Termux:**
   - For PHP script:
     ```
     apt update && apt upgrade
     apt install php
     php script.php
     ```

   - For Java program:
     ```
     apt update && apt upgrade
     apt install default-jdk
     javac Script.java
     java Script
     ```

   - For Python script:
     ```
     apt update && apt upgrade
     apt install python
     python script.py
     ```

   - For Ruby script:
     ```
     apt update && apt upgrade
     apt install ruby
     ruby script.rb
     ```

#### Author:
Sunaif Adkar

#### Instagram Profile:
Follow me on Instagram: [@sunaif_adkar](https://www.instagram.com/sunaif_adkar/)

Feel free to reach out if you have any questions or need further assistance!
