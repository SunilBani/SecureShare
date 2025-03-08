# SecureShare

# Secure File Transfer with Asymmetric Encryption

This project implements "secure file transfer" using "asymmetric encryption (RSA)".  
It ensures "confidentiality" by encrypting files before transfer and "integrity" by allowing decryption only with the recipient's private key.  

## 🚀 Features
 "RSA-based "Public-Private Key Encryption"  
 "Secure "File Encryption & Decryption" 
 "Hybrid Encryption" (AES + RSA for performance)"  
 "File Transfer Over Network" (TCP-based)"  
  "Digital Signatures" for Authentication" 

## 📌 Setup & Installation

### Install Dependencies"
Before running, install the required libraries:  
pip install pycryptodome (PyCryptodome is a Python library for implementing cryptographic algorithms like AES, RSA, and SHA securely.)

 TO EXECUTE THIS PROJECT IN GO TO COMMAND PROMPT AND FOLLOW BELOW STEPS 

 1.Generate RSA Keys

    python keygen.py      

 2.Encrypt a File (Sender)

    python sender.py test.txt   

 3.Transfer File Over Network(if you want to transfer on local machines)

   3.1 Start the Receiver (Server Side)

       python server.py

   3.2 Send the File (Sender Side)
     
       python client.py
       
 4.Decrypt the File (Receiver)
       
      python receiver.py test.enc

      

    
