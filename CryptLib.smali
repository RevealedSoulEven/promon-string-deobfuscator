.class public final Lcom/souleven/Helper/CryptLib;
.super Ljava/lang/Object;
.source "SourceFile"


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/souleven/Helper/CryptLib$EncryptMode;
    }
.end annotation


# instance fields
.field public final a:Ljavax/crypto/Cipher;

.field public final b:[B

.field public final c:[B


# direct methods
.method public constructor <init>()V
    .registers 5
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/security/NoSuchAlgorithmException;,
            Ljavax/crypto/NoSuchPaddingException;
        }
    .end annotation

    .line 1
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 2
    .line 3
    .line 4
    const/16 v1, 0x14

    new-array v0, v1, [C

    const/16 v2, 0x600d

    xor-int/lit16 v2, v2, 0x605e

    int-to-char v2, v2

    const v1, 0x2

    aput-char v2, v0, v1

    const v1, 0x2

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x12

    int-to-char v2, v2

    const v1, 0x0

    aput-char v2, v0, v1

    const v1, 0x0

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x26

    int-to-char v2, v2

    const v1, 0x13

    aput-char v2, v0, v1

    const v1, 0x2

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x0

    int-to-char v2, v2

    const v1, 0xb

    aput-char v2, v0, v1

    const v1, 0x13

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x24

    int-to-char v2, v2

    const v1, 0x6

    aput-char v2, v0, v1

    const v1, 0x0

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x6e

    int-to-char v2, v2

    const v1, 0x7

    aput-char v2, v0, v1

    const v1, 0x7

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x46

    int-to-char v2, v2

    const v1, 0x11

    aput-char v2, v0, v1

    const v1, 0x7

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x6a

    int-to-char v2, v2

    const v1, 0x1

    aput-char v2, v0, v1

    const v1, 0x11

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x46

    int-to-char v2, v2

    const v1, 0x3

    aput-char v2, v0, v1

    const v1, 0x2

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x37

    int-to-char v2, v2

    const v1, 0x10

    aput-char v2, v0, v1

    const v1, 0xb

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x66

    int-to-char v2, v2

    const v1, 0xc

    aput-char v2, v0, v1

    const v1, 0x3

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x4b

    int-to-char v2, v2

    const v1, 0xf

    aput-char v2, v0, v1

    const v1, 0xc

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x65

    int-to-char v2, v2

    const v1, 0x8

    aput-char v2, v0, v1

    const v1, 0x8

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x0

    int-to-char v2, v2

    const v1, 0xd

    aput-char v2, v0, v1

    const v1, 0xf

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x26

    int-to-char v2, v2

    const v1, 0x5

    aput-char v2, v0, v1

    const v1, 0x6

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x0

    int-to-char v2, v2

    const v1, 0xa

    aput-char v2, v0, v1

    const v1, 0xd

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x31

    int-to-char v2, v2

    const v1, 0xe

    aput-char v2, v0, v1

    const v1, 0xa

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x0

    int-to-char v2, v2

    const v1, 0x4

    aput-char v2, v0, v1

    const v1, 0x3

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x64

    int-to-char v2, v2

    const v1, 0x9

    aput-char v2, v0, v1

    const v1, 0xc

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x5b

    int-to-char v2, v2

    const v1, 0x12

    aput-char v2, v0, v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object v3

    .line 5
    .line 6
    invoke-static {v3}, Ljavax/crypto/Cipher;->getInstance(Ljava/lang/String;)Ljavax/crypto/Cipher;

    .line 7
    .line 8
    .line 9
    move-result-object v3

    .line 10
    iput-object v3, p0, Lcom/souleven/Helper/CryptLib;->a:Ljavax/crypto/Cipher;

    .line 11
    .line 12
    const/16 v3, 0x20

    .line 13
    .line 14
    new-array v3, v3, [B

    .line 15
    .line 16
    iput-object v3, p0, Lcom/souleven/Helper/CryptLib;->b:[B

    .line 17
    .line 18
    const/16 v3, 0x10

    .line 19
    .line 20
    new-array v3, v3, [B

    .line 21
    .line 22
    iput-object v3, p0, Lcom/souleven/Helper/CryptLib;->c:[B

    .line 23
    .line 24
    return-void
.end method

.method public static a(Ljava/lang/String;)Ljava/lang/String;
    .registers 10
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/security/NoSuchAlgorithmException;,
            Ljava/io/UnsupportedEncodingException;
        }
    .end annotation

    .line 1
    const/16 v1, 0x7

    new-array v0, v1, [C

    const/16 v2, -0x7440

    xor-int/lit16 v2, v2, -0x740a

    int-to-char v2, v2

    const v1, 0x6

    aput-char v2, v0, v1

    const v1, 0x6

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x4

    int-to-char v2, v2

    const v1, 0x4

    aput-char v2, v0, v1

    const v1, 0x6

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x7e

    int-to-char v2, v2

    const v1, 0x1

    aput-char v2, v0, v1

    const v1, 0x6

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x77

    int-to-char v2, v2

    const v1, 0x2

    aput-char v2, v0, v1

    const v1, 0x1

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x7d

    int-to-char v2, v2

    const v1, 0x5

    aput-char v2, v0, v1

    const v1, 0x4

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x1f

    int-to-char v2, v2

    const v1, 0x3

    aput-char v2, v0, v1

    const v1, 0x2

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x12

    int-to-char v2, v2

    const v1, 0x0

    aput-char v2, v0, v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object v3

    .line 2
    .line 3
    invoke-static {v3}, Ljava/security/MessageDigest;->getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;

    .line 4
    .line 5
    .line 6
    move-result-object v3

    .line 7
    sget-object v4, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 8
    .line 9
    invoke-virtual {p0, v4}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 10
    .line 11
    .line 12
    move-result-object p0

    .line 13
    invoke-virtual {v3, p0}, Ljava/security/MessageDigest;->update([B)V

    .line 14
    .line 15
    .line 16
    invoke-virtual {v3}, Ljava/security/MessageDigest;->digest()[B

    .line 17
    .line 18
    .line 19
    move-result-object p0

    .line 20
    new-instance v3, Ljava/lang/StringBuilder;

    .line 21
    .line 22
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    .line 23
    .line 24
    .line 25
    array-length v4, p0

    .line 26
    const/4 v5, 0x0

    .line 27
    move v6, v5

    .line 28
    :goto_7e
    if-ge v6, v4, :cond_d3

    .line 29
    .line 30
    aget-byte v7, p0, v6

    .line 31
    .line 32
    const/4 v8, 0x1

    .line 33
    new-array v8, v8, [Ljava/lang/Object;

    .line 34
    .line 35
    invoke-static {v7}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    .line 36
    .line 37
    .line 38
    move-result-object v7

    .line 39
    aput-object v7, v8, v5

    .line 40
    .line 41
    const/16 v1, 0x4

    new-array v0, v1, [C

    const/16 v2, 0x296

    xor-int/lit16 v2, v2, 0x2ee

    int-to-char v2, v2

    const v1, 0x3

    aput-char v2, v0, v1

    const v1, 0x3

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x4a

    int-to-char v2, v2

    const v1, 0x2

    aput-char v2, v0, v1

    const v1, 0x3

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x5d

    int-to-char v2, v2

    const v1, 0x0

    aput-char v2, v0, v1

    const v1, 0x0

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x15

    int-to-char v2, v2

    const v1, 0x1

    aput-char v2, v0, v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object v7

    .line 42
    .line 43
    invoke-static {v7, v8}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    .line 44
    .line 45
    .line 46
    move-result-object v7

    .line 47
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 48
    .line 49
    .line 50
    add-int/lit8 v6, v6, 0x1

    .line 51
    .line 52
    goto :goto_7e

    .line 53
    :cond_d3
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    .line 54
    .line 55
    .line 56
    move-result-object p0

    .line 57
    invoke-virtual {p0}, Ljava/lang/String;->length()I

    .line 58
    .line 59
    .line 60
    move-result p0

    .line 61
    const/16 v4, 0x20

    .line 62
    .line 63
    if-le v4, p0, :cond_e4

    .line 64
    .line 65
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    .line 66
    .line 67
    .line 68
    move-result-object p0

    .line 69
    goto :goto_e8

    .line 70
    :cond_e4
    invoke-virtual {v3, v5, v4}, Ljava/lang/StringBuilder;->substring(II)Ljava/lang/String;

    .line 71
    .line 72
    .line 73
    move-result-object p0

    .line 74
    :goto_e8
    return-object p0
.end method

.method public static e()Ljava/lang/String;
    .registers 10

    .line 1
    new-instance v3, Ljava/security/SecureRandom;

    .line 2
    .line 3
    invoke-direct {v3}, Ljava/security/SecureRandom;-><init>()V

    .line 4
    .line 5
    .line 6
    const/16 v4, 0x10

    .line 7
    .line 8
    new-array v5, v4, [B

    .line 9
    .line 10
    invoke-virtual {v3, v5}, Ljava/security/SecureRandom;->nextBytes([B)V

    .line 11
    .line 12
    .line 13
    new-instance v3, Ljava/lang/StringBuilder;

    .line 14
    .line 15
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    .line 16
    .line 17
    .line 18
    const/4 v6, 0x0

    .line 19
    move v7, v6

    .line 20
    :goto_13
    if-ge v7, v4, :cond_68

    .line 21
    .line 22
    aget-byte v8, v5, v7

    .line 23
    .line 24
    const/4 v9, 0x1

    .line 25
    new-array v9, v9, [Ljava/lang/Object;

    .line 26
    .line 27
    invoke-static {v8}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    .line 28
    .line 29
    .line 30
    move-result-object v8

    .line 31
    aput-object v8, v9, v6

    .line 32
    .line 33
    const/16 v1, 0x4

    new-array v0, v1, [C

    const/16 v2, 0x1436

    xor-int/lit16 v2, v2, 0x1404

    int-to-char v2, v2

    const v1, 0x2

    aput-char v2, v0, v1

    const v1, 0x2

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x2

    int-to-char v2, v2

    const v1, 0x1

    aput-char v2, v0, v1

    const v1, 0x2

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x4a

    int-to-char v2, v2

    const v1, 0x3

    aput-char v2, v0, v1

    const v1, 0x1

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x15

    int-to-char v2, v2

    const v1, 0x0

    aput-char v2, v0, v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object v8

    .line 34
    .line 35
    invoke-static {v8, v9}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    .line 36
    .line 37
    .line 38
    move-result-object v8

    .line 39
    invoke-virtual {v3, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 40
    .line 41
    .line 42
    add-int/lit8 v7, v7, 0x1

    .line 43
    .line 44
    goto :goto_13

    .line 45
    :cond_68
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    .line 46
    .line 47
    .line 48
    move-result-object v5

    .line 49
    invoke-virtual {v5}, Ljava/lang/String;->length()I

    .line 50
    .line 51
    .line 52
    move-result v5

    .line 53
    if-le v4, v5, :cond_77

    .line 54
    .line 55
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    .line 56
    .line 57
    .line 58
    move-result-object v3

    .line 59
    return-object v3

    .line 60
    :cond_77
    invoke-virtual {v3, v6, v4}, Ljava/lang/StringBuilder;->substring(II)Ljava/lang/String;

    .line 61
    .line 62
    .line 63
    move-result-object v3

    .line 64
    return-object v3
.end method


# virtual methods
.method public final b(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 8

    .line 1
    if-eqz p1, :cond_22

    .line 2
    .line 3
    :try_start_2
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    .line 4
    .line 5
    .line 6
    move-result v3

    .line 7
    if-lez v3, :cond_22

    .line 8
    .line 9
    invoke-static {p2}, Lcom/souleven/Helper/CryptLib;->a(Ljava/lang/String;)Ljava/lang/String;

    .line 10
    .line 11
    .line 12
    move-result-object p2

    .line 13
    sget-object v3, Lcom/souleven/Helper/CryptLib$EncryptMode;->DECRYPT:Lcom/souleven/Helper/CryptLib$EncryptMode;

    .line 14
    .line 15
    invoke-static {}, Lcom/souleven/Helper/CryptLib;->e()Ljava/lang/String;

    .line 16
    .line 17
    .line 18
    move-result-object v4

    .line 19
    invoke-virtual {p0, p1, p2, v3, v4}, Lcom/souleven/Helper/CryptLib;->c(Ljava/lang/String;Ljava/lang/String;Lcom/souleven/Helper/CryptLib$EncryptMode;Ljava/lang/String;)[B

    .line 20
    .line 21
    .line 22
    move-result-object p1

    .line 23
    new-instance p2, Ljava/lang/String;

    .line 24
    .line 25
    invoke-direct {p2, p1}, Ljava/lang/String;-><init>([B)V

    .line 26
    .line 27
    .line 28
    const/16 p1, 0x10

    .line 29
    .line 30
    invoke-virtual {p2, p1}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    .line 31
    .line 32
    .line 33
    move-result-object p1
    :try_end_21
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_21} :catch_22

    .line 34
    return-object p1

    .line 35
    :catch_22
    :cond_22
    const/16 v1, 0x0

    new-array v0, v1, [C

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object p1

    .line 36
    .line 37
    return-object p1
.end method

.method public final c(Ljava/lang/String;Ljava/lang/String;Lcom/souleven/Helper/CryptLib$EncryptMode;Ljava/lang/String;)[B
    .registers 14
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/io/UnsupportedEncodingException;,
            Ljava/security/InvalidKeyException;,
            Ljava/security/InvalidAlgorithmParameterException;,
            Ljavax/crypto/IllegalBlockSizeException;,
            Ljavax/crypto/BadPaddingException;,
            Ljava/lang/Exception;
        }
    .end annotation

    .line 1
    sget-object v3, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 2
    .line 3
    invoke-virtual {p2, v3}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 4
    .line 5
    .line 6
    move-result-object v3

    .line 7
    array-length v3, v3

    .line 8
    sget-object v4, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 9
    .line 10
    invoke-virtual {p2, v4}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 11
    .line 12
    .line 13
    move-result-object v4

    .line 14
    array-length v4, v4

    .line 15
    iget-object v5, p0, Lcom/souleven/Helper/CryptLib;->b:[B

    .line 16
    .line 17
    array-length v6, v5

    .line 18
    if-le v4, v6, :cond_14

    .line 19
    .line 20
    array-length v3, v5

    .line 21
    :cond_14
    sget-object v4, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 22
    .line 23
    invoke-virtual {p4, v4}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 24
    .line 25
    .line 26
    move-result-object v4

    .line 27
    array-length v4, v4

    .line 28
    sget-object v6, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 29
    .line 30
    invoke-virtual {p4, v6}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 31
    .line 32
    .line 33
    move-result-object v6

    .line 34
    array-length v6, v6

    .line 35
    iget-object v7, p0, Lcom/souleven/Helper/CryptLib;->c:[B

    .line 36
    .line 37
    array-length v8, v7

    .line 38
    if-le v6, v8, :cond_28

    .line 39
    .line 40
    array-length v4, v7

    .line 41
    :cond_28
    sget-object v6, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 42
    .line 43
    invoke-virtual {p2, v6}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 44
    .line 45
    .line 46
    move-result-object p2

    .line 47
    const/4 v6, 0x0

    .line 48
    invoke-static {p2, v6, v5, v6, v3}, Ljava/lang/System;->arraycopy(Ljava/lang/Object;ILjava/lang/Object;II)V

    .line 49
    .line 50
    .line 51
    sget-object p2, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 52
    .line 53
    invoke-virtual {p4, p2}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 54
    .line 55
    .line 56
    move-result-object p2

    .line 57
    invoke-static {p2, v6, v7, v6, v4}, Ljava/lang/System;->arraycopy(Ljava/lang/Object;ILjava/lang/Object;II)V

    .line 58
    .line 59
    .line 60
    new-instance p2, Ljavax/crypto/spec/SecretKeySpec;

    .line 61
    .line 62
    const/16 v1, 0x3

    new-array v0, v1, [C

    const/16 v2, 0x1c4d

    xor-int/lit16 v2, v2, 0x1c08

    int-to-char v2, v2

    const v1, 0x1

    aput-char v2, v0, v1

    const v1, 0x1

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x4

    int-to-char v2, v2

    const v1, 0x0

    aput-char v2, v0, v1

    const v1, 0x1

    aget-char v2, v0, v1

    xor-int/lit16 v2, v2, 0x16

    int-to-char v2, v2

    const v1, 0x2

    aput-char v2, v0, v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object p4

    .line 63
    .line 64
    invoke-direct {p2, v5, p4}, Ljavax/crypto/spec/SecretKeySpec;-><init>([BLjava/lang/String;)V

    .line 65
    .line 66
    .line 67
    new-instance p4, Ljavax/crypto/spec/IvParameterSpec;

    .line 68
    .line 69
    invoke-direct {p4, v7}, Ljavax/crypto/spec/IvParameterSpec;-><init>([B)V

    .line 70
    .line 71
    .line 72
    sget-object v3, Lcom/souleven/Helper/CryptLib$EncryptMode;->ENCRYPT:Lcom/souleven/Helper/CryptLib$EncryptMode;

    .line 73
    .line 74
    invoke-virtual {p3, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    .line 75
    .line 76
    .line 77
    move-result p3

    .line 78
    iget-object v3, p0, Lcom/souleven/Helper/CryptLib;->a:Ljavax/crypto/Cipher;

    .line 79
    .line 80
    if-eqz p3, :cond_8f

    .line 81
    .line 82
    const/4 p3, 0x1

    .line 83
    invoke-virtual {v3, p3, p2, p4}, Ljavax/crypto/Cipher;->init(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V

    .line 84
    .line 85
    .line 86
    sget-object p2, Ljava/nio/charset/StandardCharsets;->UTF_8:Ljava/nio/charset/Charset;

    .line 87
    .line 88
    invoke-virtual {p1, p2}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B

    .line 89
    .line 90
    .line 91
    move-result-object p1

    .line 92
    invoke-virtual {v3, p1}, Ljavax/crypto/Cipher;->doFinal([B)[B

    .line 93
    .line 94
    .line 95
    move-result-object p1

    .line 96
    return-object p1

    .line 97
    :cond_8f
    const/4 p3, 0x2

    .line 98
    invoke-virtual {v3, p3, p2, p4}, Ljavax/crypto/Cipher;->init(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V

    .line 99
    .line 100
    .line 101
    invoke-virtual {p1}, Ljava/lang/String;->getBytes()[B

    .line 102
    .line 103
    .line 104
    move-result-object p1

    .line 105
    invoke-static {p1, v6}, Landroid/util/Base64;->decode([BI)[B

    .line 106
    .line 107
    .line 108
    move-result-object p1

    .line 109
    invoke-virtual {v3, p1}, Ljavax/crypto/Cipher;->doFinal([B)[B

    .line 110
    .line 111
    .line 112
    move-result-object p1

    .line 113
    return-object p1
.end method

.method public final d(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 8

    .line 1
    :try_start_0
    new-instance v3, Ljava/lang/StringBuilder;

    .line 2
    .line 3
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    .line 4
    .line 5
    .line 6
    invoke-static {}, Lcom/souleven/Helper/CryptLib;->e()Ljava/lang/String;

    .line 7
    .line 8
    .line 9
    move-result-object v4

    .line 10
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 11
    .line 12
    .line 13
    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 14
    .line 15
    .line 16
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    .line 17
    .line 18
    .line 19
    move-result-object p1

    .line 20
    invoke-static {p2}, Lcom/souleven/Helper/CryptLib;->a(Ljava/lang/String;)Ljava/lang/String;

    .line 21
    .line 22
    .line 23
    move-result-object p2

    .line 24
    sget-object v3, Lcom/souleven/Helper/CryptLib$EncryptMode;->ENCRYPT:Lcom/souleven/Helper/CryptLib$EncryptMode;

    .line 25
    .line 26
    invoke-static {}, Lcom/souleven/Helper/CryptLib;->e()Ljava/lang/String;

    .line 27
    .line 28
    .line 29
    move-result-object v4

    .line 30
    invoke-virtual {p0, p1, p2, v3, v4}, Lcom/souleven/Helper/CryptLib;->c(Ljava/lang/String;Ljava/lang/String;Lcom/souleven/Helper/CryptLib$EncryptMode;Ljava/lang/String;)[B

    .line 31
    .line 32
    .line 33
    move-result-object p1

    .line 34
    const/4 p2, 0x0

    .line 35
    invoke-static {p1, p2}, Landroid/util/Base64;->encodeToString([BI)Ljava/lang/String;

    .line 36
    .line 37
    .line 38
    move-result-object p1
    :try_end_26
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_26} :catch_27

    .line 39
    return-object p1

    .line 40
    :catch_27
    const/16 v1, 0x0

    new-array v0, v1, [C

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v2}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object p1

    .line 41
    .line 42
    return-object p1
.end method
