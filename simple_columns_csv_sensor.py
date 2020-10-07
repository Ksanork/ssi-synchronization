import csv

INITIAL_OFFSET = -200


def read_from_file(vars, opts):
    headers_ln = opts['headers_ln']
    path = opts['path']
    auto_init = opts['auto_init']

    with open(path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        if headers_ln >= 2 and auto_init == 1:
            # date
            vars['initial_timestamp'] = next(csv_reader)[0]

            # rate
            vars['sr'] = next(csv_reader)[0]
        else:
            for i in range(headers_ln):
                next(csv_reader)

        output = []
        for row in csv_reader:
            output.append(float(row[0]))

        return output


def getOptions(opts, vars):
    opts['path'] = ''
    opts['sr'] = -1.0
    opts['name'] = 'diagram_channel'
    opts['offset'] = 0
    opts['headers_ln'] = 2
    opts['auto_init'] = 1


def getChannelNames(opts, vars):
    return { 'csv_data' : '' }


def initChannel(name, channel, types, opts, vars):
    if opts['path'] == '':
        print('[csv_sensor] empty path')

    if name == 'csv_data':
        vars['hr'] = read_from_file(vars, opts)

        channel.dim = 1
        channel.type = types.FLOAT
        channel.sr = opts['sr'] if opts['sr'] != -1 else vars['sr']
    else:
        print('[csv_sensor] unkown channel name')


def connect(opts, vars):
    vars['pos'] = INITIAL_OFFSET + opts['offset']


def read(name, sout, reset, board, opts, vars):
    hr = vars['hr']
    pos = vars['pos']

    if name == 'csv_data':
        for n in range(sout.num):
            if pos < len(hr):
                sout[n] = hr[pos]
                pos += 1

    else:
        print('[csv_sensor] unkown channel name')

    vars['pos'] = pos


def disconnect(opts, vars):
    pass
