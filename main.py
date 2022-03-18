from jwcrypto import jwk

key = jwk.JWK.generate(kty='RSA', size=2048, alg='RSA256', use='enc', kid='ya-dev')
public_key = key.export_public()
private_key = key.export_private()

print(public_key)
print(private_key)

f = open("private.key", "a")
f.write(private_key)
f.close()

f2 = open("public.key", "a")
f2.write(public_key)
f2.close()
