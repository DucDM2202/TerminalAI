import obfuscation_detection as od

oc = od.ObfuscationClassifier(od.PlatformType.ALL)
commands = ['cmd.exe /c "echo Invoke-DOSfuscation"',
            'cm%windir:~ -4, -3%.e^Xe,;^,/^C",;,S^Et ^^o^=fus^cat^ion&,;,^se^T ^ ^ ^B^=o^ke-D^OS&&,;,s^Et^^ d^=ec^ho I^nv&&,;,C^Al^l,;,^%^D%^%B%^%o^%"',
            'cat /etc/passwd']
classifications = oc(commands)

# 1 is obfuscated, 0 is non-obfuscated
print(classifications) # [0, 1, 0]