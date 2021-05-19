from fastecdsa import keys, curve,ecdsa

privateKey, publicKey = keys.gen_keypair(curve.P256) 

#dummy message
msg = "Hey, please encrypt me"

# generating signature
signature = ecdsa.sign(msg, privateKey)

# verify signature
valid = ecdsa.verify(signature, msg, publicKey, curve.P256)

# used P256 instead of secp256k1 since the library not giving proper results