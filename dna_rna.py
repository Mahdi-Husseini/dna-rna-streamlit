from msilib import sequence
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna.jpg')

st.image(image, use_column_width= True)

st.write("""
# DNA to RNA _ Nucleotide Count App

This app converts DNA to RNA and counts the nucleotides

***""")

st.sidebar.header('the sequence by default is set non_transcribed, if transcribed:')
trans = st.sidebar.checkbox('transcribed')


def verifier(seq):
    l = list(seq.upper())
    b = True
    for i in range(len(l)):
        if l[i] in ['A','G','T','C']:
            continue
        b = False
        break
    return b

st.header('Enter DNA Sequence:')
sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
# sequence_sidebar = st.sidebar.text_area("sequence input", sequence_input, height = 250)
seq = st.text_area("sequence input", sequence_input, height = 250)
seq = seq.splitlines()  
seq = ''.join(seq)

if not verifier(seq):
    st.header('Please enter a valid sequence')

st.write("""
***
""")

st.header('The entered DNA query:')
seq


def DNA_Count(seq):
    seq = seq.upper()
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('C',seq.count('C')),
        ('G',seq.count('G'))
    ])
    return d

def RNA_Count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('U', seq.count('U')),
        ('C', seq.count('C')),
        ('G', seq.count('G'))
    ])
    return d

def RNA_convert(seq):
    l = list(seq.upper())
    for i in range(len(l)):
        if l[i] == 'T':
            l[i] = 'U'
    return l

def transcriber(seq):
    l = list(seq.upper())
    for i in range(len(l)):
        if l[i] == 'T':
            l[i] = 'A'
        elif l[i] == 'A':
            l[i] = 'T'
        elif l[i] == 'G':
            l[i] = 'C'
        elif l[i] == 'C':
            l[i] = 'G'
        else:
            l = list("invalid input")
            break
    return l

x = DNA_Count(seq)

st.subheader('Sum of nucleotides: ' + str(x['A'] + x['C'] + x['G'] + x['T']))

st.header('DNA Nucleotide Count:')

if trans and verifier(seq):
    st.subheader('1. Dictionary Format')

    x

    st.subheader('2. Text Format')
    st.write('There are:  ' + str(x['A']) + ' adenine (A)')
    st.write(str(x['T']) + ' thymine (T)')
    st.write(str(x['G']) + ' guanine (G)')
    st.write(str(x['C']) + ' cytosine (C)')

    st.subheader('3. DataFrame Format: ')
    df = pd.DataFrame.from_dict(x, orient="index")
    df = df.rename({0: 'count'}, axis = 'columns')
    df.reset_index(inplace = True)
    df = df.rename(columns = {'index':'nucleotide'})
    st.write(df)

    st.subheader('4. Bar Chart Format: ')
    f = alt.Chart(df).mark_bar().encode(
        x = 'nucleotide',
        y = 'count'
    )

    f = f.properties(
        width = alt.Step(75)
    )

    st.write(f)

    st.write('''
        ***
        ''')
    
    st.header('RNA Sequence: ')
    rna = ""
    for i in RNA_convert(seq):
        rna += i
    rna

    x = RNA_Count(rna)
    st.subheader('1. Dictionary Format: ')
    x

    st.subheader('2. Text Format')
    st.write('There are:  ' + str(x['A']) + ' adenine (A)')
    st.write(str(x['U']) + ' uracil (U)')
    st.write(str(x['G']) + ' guanine (G)')
    st.write(str(x['C']) + ' cytosine (C)')

    st.subheader('3. DataFrame Format: ')
    df = pd.DataFrame.from_dict(x, orient="index")
    df = df.rename({0: 'count'}, axis = 'columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'nucleotide'})
    st.write(df)

    st.subheader('4. Bar Chart Format: ')
    f = alt.Chart(df).mark_bar().encode(
        x = "nucleotide",
        y = "count"
    )

    f = f.properties(
        width = alt.Step(75)
    )
    st.write(f)

elif not trans and verifier(seq):
    st.subheader('1. Dictionary Format')

    x

    st.subheader('2. Text Format')
    st.write('There are:  ' + str(x['A']) + ' adenine (A)')
    st.write(str(x['T']) + ' thymine (T)')
    st.write(str(x['G']) + ' guanine (G)')
    st.write(str(x['C']) + ' cytosine (C)')

    st.subheader('3. DataFrame Format: ')
    df = pd.DataFrame.from_dict(x, orient="index")
    df = df.rename({0: 'count'}, axis = 'columns')
    df.reset_index(inplace = True)
    df = df.rename(columns = {'index':'nucleotide'})
    st.write(df)

    st.subheader('4. Bar Chart Format: ')
    f = alt.Chart(df).mark_bar().encode(
        x = 'nucleotide',
        y = 'count'
    )

    f = f.properties(
        width = alt.Step(75)
    )

    st.write(f)

    st.write('''
        ***
        ''')

    st.header('DNA Transcribed Sequence: ')

    t = ""
    for i in transcriber(seq):
        t += i
    t

    st.subheader('1. Dictionary Format')

    x = DNA_Count(t)
    x

    st.subheader('2. Text Format')
    st.write('There are:  ' + str(x['A']) + ' adenine (A)')
    st.write(str(x['T']) + ' thymine (T)')
    st.write(str(x['G']) + ' guanine (G)')
    st.write(str(x['C']) + ' cytosine (C)')

    st.subheader('3. DataFrame Format: ')
    df = pd.DataFrame.from_dict(x, orient="index")
    df = df.rename({0: 'count'}, axis = 'columns')
    df.reset_index(inplace = True)
    df = df.rename(columns = {'index':'nucleotide'})
    st.write(df)

    st.subheader('4. Bar Chart Format: ')
    f = alt.Chart(df).mark_bar().encode(
        x = 'nucleotide',
        y = 'count'
    )

    f = f.properties(
        width = alt.Step(75)
    )

    st.write(f)

    st.write('''
        ***
        ''')
    
    st.header('RNA Sequence: ')
    rna = ""
    for i in RNA_convert(t):
        rna += i
    rna

    x = RNA_Count(rna)
    st.subheader('1. Dictionary Format: ')
    x

    st.subheader('2. Text Format')
    st.write('There are:  ' + str(x['A']) + ' adenine (A)')
    st.write(str(x['U']) + ' uracil (U)')
    st.write(str(x['G']) + ' guanine (G)')
    st.write(str(x['C']) + ' cytosine (C)')

    st.subheader('3. DataFrame Format: ')
    df = pd.DataFrame.from_dict(x, orient="index")
    df = df.rename({0: 'count'}, axis = 'columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'nucleotide'})
    st.write(df)

    st.subheader('4. Bar Chart Format: ')
    f = alt.Chart(df).mark_bar().encode(
        x = "nucleotide",
        y = "count"
    )

    f = f.properties(
        width = alt.Step(75)
    )
    st.write(f)



    
    

