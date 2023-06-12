import aiml
k = aiml.Kernel()




# Load AIML files and bootstrap the kernel
k.bootstrap(learnFiles="standard\*.aiml")

# Optionally, save the learned session for future use
k.saveBrain("brain.brn")
while 1:
    print(k.respond(input("Message: "))) 