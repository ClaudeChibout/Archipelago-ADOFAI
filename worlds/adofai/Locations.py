from typing import NamedTuple
class LocData(NamedTuple):
    id: int
    world: str | None


adofai_locations = {
    "1-1": LocData(98765401, "World 1"),
    "1-2": LocData(98765402, "World 1"),
    "1-3": LocData(98765403, "World 1"),
    "1-4": LocData(98765404, "World 1"),
    "1-5": LocData(98765405, "World 1"),
    "1-6": LocData(98765406, "World 1"),
    "1-X": LocData(98765407, "World 1"),
}

MainWorldsLoc = {
    # "1-X": LocData(98765407, "World 1"),
    "2-X": LocData(98765412, "World 2"),
    "3-X": LocData(98765419, "World 3"),
    "4-X": LocData(98765425, "World 4"),
    "5-X": LocData(98765430, "World 5"),
    "6-X": LocData(98765435, "World 6"),
    "7-X": LocData(98765441, "World 7"),
    "8-X": LocData(98765450, "World 8"),
    "9-X": LocData(98765456, "World 9"),
    "10-X": LocData(98765465, "World 10"),
    "11-X": LocData(98765472, "World 11"),
    "12-X": LocData(98765479, "World 12"),
}

MainWorldsTutoLoc = {
    # "1-1": LocData(98765401, "World 1"),
    # "1-2": LocData(98765402, "World 1"),
    # "1-3": LocData(98765403, "World 1"),
    # "1-4": LocData(98765404, "World 1"),
    # "1-5": LocData(98765405, "World 1"),
    # "1-6": LocData(98765406, "World 1"),

    "2-1": LocData(98765408, "World 2"),
    "2-2": LocData(98765409, "World 2"),
    "2-3": LocData(98765410, "World 2"),

    "3-1": LocData(98765413, "World 3"),
    "3-2": LocData(98765414, "World 3"),
    "3-3": LocData(98765415, "World 3"),
    "3-4": LocData(98765416, "World 3"),
    "3-5": LocData(98765417, "World 3"),
    "3-6": LocData(98765418, "World 3"),

    "4-1": LocData(98765420, "World 4"),
    "4-2": LocData(98765421, "World 4"),
    "4-3": LocData(98765422, "World 4"),
    "4-4": LocData(98765423, "World 4"),
    "4-5": LocData(98765424, "World 4"),

    "5-1": LocData(98765426, "World 5"),
    "5-2": LocData(98765427, "World 5"),
    "5-3": LocData(98765428, "World 5"),
    "5-4": LocData(98765429, "World 5"),

    "6-1": LocData(98765431, "World 6"),
    "6-2": LocData(98765432, "World 6"),
    "6-3": LocData(98765433, "World 6"),
    "6-4": LocData(98765434, "World 6"),

    "7-1": LocData(98765436, "World 7"),
    "7-2": LocData(98765437, "World 7"),
    "7-3": LocData(98765438, "World 7"),
    "7-4": LocData(98765439, "World 7"),
    "7-5": LocData(98765440, "World 7"),

    "8-1": LocData(98765442, "World 8"),
    "8-2": LocData(98765443, "World 8"),
    "8-3": LocData(98765444, "World 8"),
    "8-4": LocData(98765445, "World 8"),
    "8-5": LocData(98765446, "World 8"),
    "8-6": LocData(98765447, "World 8"),
    "8-7": LocData(98765448, "World 8"),
    "8-8": LocData(98765449, "World 8"),

    "9-1": LocData(98765451, "World 9"),
    "9-2": LocData(98765452, "World 9"),
    "9-3": LocData(98765453, "World 9"),
    "9-4": LocData(98765454, "World 9"),
    "9-5": LocData(98765455, "World 9"),

    "10-1": LocData(98765457, "World 10"),
    "10-2": LocData(98765458, "World 10"),
    "10-3": LocData(98765459, "World 10"),
    "10-4": LocData(98765460, "World 10"),
    "10-5": LocData(98765461, "World 10"),
    "10-6": LocData(98765462, "World 10"),
    "10-7": LocData(98765463, "World 10"),
    "10-8": LocData(98765464, "World 10"),

    "11-1": LocData(98765466, "World 11"),
    "11-2": LocData(98765467, "World 11"),
    "11-3": LocData(98765468, "World 11"),
    "11-4": LocData(98765469, "World 11"),
    "11-5": LocData(98765470, "World 11"),
    "11-6": LocData(98765471, "World 11"),

    "12-1": LocData(98765473, "World 12"),
    "12-2": LocData(98765474, "World 12"),
    "12-3": LocData(98765475, "World 12"),
    "12-4": LocData(98765476, "World 12"),
    "12-5": LocData(98765477, "World 12"),
    "12-6": LocData(98765478, "World 12"),
}

XtraWorldsLoc = {
    "XS-X": LocData(98765485, "World XS"),
    "PA-X": LocData(98765486, "World PA"),
    "XH-X": LocData(98765487, "World XH"),
    "XC-X": LocData(98765488, "World XC"),
    "XF-X": LocData(98765489, "World XF"),
    "XR-X": LocData(98765490, "World XR"),
    "RJ-X": LocData(98765491, "World RJ"),
    "XN-X": LocData(98765492, "World XN"),
    "XM-X": LocData(98765493, "World XM"),
}

XtraTutoLoc = {
    "XS-1": LocData(98765500, "World XS"),
    "XS-2": LocData(98765501, "World XS"),
    "XS-3": LocData(98765502, "World XS"),
    "XS-4": LocData(98765503, "World XS"),
    "XS-5": LocData(98765504, "World XS"),
    "XS-6": LocData(98765505, "World XS"),
    "XS-7": LocData(98765506, "World XS"),
    "XS-8": LocData(98765507, "World XS"),

    "PA-1": LocData(98765508, "World PA"),

    "XH-1": LocData(98765509, "World XH"),
    "XH-2": LocData(98765510, "World XH"),
    "XH-3": LocData(98765511, "World XH"),

    "XC-1": LocData(98765512, "World XC"),
    "XC-2": LocData(98765513, "World XC"),
    "XC-3": LocData(98765514, "World XC"),
    "XC-4": LocData(98765515, "World XC"),
    "XC-5": LocData(98765516, "World XC"),

    "XF-1": LocData(98765517, "World XF"),
    "XF-2": LocData(98765518, "World XF"),
    "XF-3": LocData(98765519, "World XF"),

    "XR-1": LocData(98765520, "World XR"),
    "XR-2": LocData(98765521, "World XR"),
    "XR-3": LocData(98765522, "World XR"),

    "RJ-1": LocData(98765523, "World RJ"),
    "RJ-2": LocData(98765524, "World RJ"),
    "RJ-3": LocData(98765525, "World RJ"),
    "RJ-4": LocData(98765526, "World RJ"),
    "RJ-5": LocData(98765527, "World RJ"),
    "RJ-6": LocData(98765528, "World RJ"),
    "RJ-7": LocData(98765529, "World RJ"),

    "XN-1": LocData(98765530, "World XN"),
    "XN-2": LocData(98765531, "World XN"),
    "XN-3": LocData(98765532, "World XN"),

    "XM-1": LocData(98765533, "World XM"),
    "XM-2": LocData(98765534, "World XM"),
    "XM-3": LocData(98765535, "World XM"),
    "XM-4": LocData(98765536, "World XM"),
}


BWorldLoc = {
    "B-X": LocData(98765537, "World B"),
}

BWorldTutoLoc = {
    "B-1": LocData(98765538, "World B"),
}

CrownWorldsTutoLoc = {
    "XO-1": LocData(98765539, "World XO"),
    "XO-2": LocData(98765540, "World XO"),

    "XT-1": LocData(98765541, "World XT"),
    "XT-2": LocData(98765542, "World XT"),
    "XT-3": LocData(98765543, "World XT"),
    "XT-4": LocData(98765544, "World XT"),
    "XT-5": LocData(98765545, "World XT"),
    "XT-6": LocData(98765546, "World XT"),
    "XT-7": LocData(98765547, "World XT"),
    "XT-8": LocData(98765548, "World XT"),

    "XI-1": LocData(98765549, "World XI"),
    "XI-2": LocData(98765550, "World XI"),
    "XI-3": LocData(98765551, "World XI"),
    "XI-4": LocData(98765552, "World XI"),
    "XI-5": LocData(98765553, "World XI"),
    "XI-6": LocData(98765554, "World XI"),
    "XI-7": LocData(98765555, "World XI"),
}

CrownWorldsLoc = {
    "XO-X": LocData(98765556, "World XO"),
    "XT-X": LocData(98765557, "World XT"),
    "XI-X": LocData(98765558, "World XI"),
}

StarWorldsTutoLoc = {
    "MN-1": LocData(98765559, "World MN"),
    "MN-2": LocData(98765560, "World MN"),
    "MN-3": LocData(98765561, "World MN"),
    "MN-4": LocData(98765562, "World MN"),

    "ML-1": LocData(98765563, "World ML"),
    "ML-2": LocData(98765564, "World ML"),
    "ML-3": LocData(98765565, "World ML"),
    "ML-4": LocData(98765566, "World ML"),
    "ML-5": LocData(98765567, "World ML"),
    "ML-6": LocData(98765568, "World ML"),
    "ML-7": LocData(98765569, "World ML"),

    "MO-1": LocData(98765570, "World MO"),
    "MO-2": LocData(98765571, "World MO"),
    "MO-3": LocData(98765572, "World MO"),
}

StarWorldsLoc = {
    "MN-X": LocData(98765573, "World MN"),
    "ML-X": LocData(98765574, "World ML"),
    "MO-X": LocData(98765575, "World MO"),
}

NeonCosmosWorldsTutoLoc = {
    "T1-1": LocData(98765576, "World T1"),
    "T1-2": LocData(98765577, "World T1"),
    "T1-3": LocData(98765578, "World T1"),
    "T1-4": LocData(98765579, "World T1"),

    "T2-1": LocData(98765580, "World T2"),
    "T2-2": LocData(98765581, "World T2"),
    "T2-3": LocData(98765582, "World T2"),
    "T2-4": LocData(98765583, "World T2"),
    "T2-5": LocData(98765584, "World T2"),
    "T2-6": LocData(98765585, "World T2"),
    "T2-7": LocData(98765586, "World T2"),
    "T2-8": LocData(98765587, "World T2"),
    "T2-9": LocData(98765588, "World T2"),

    "T3-1": LocData(98765589, "World T3"),

    "T4-1": LocData(98765590, "World T4"),
    "T4-2": LocData(98765591, "World T4"),
    "T4-3": LocData(98765592, "World T4"),
    "T4-4": LocData(98765593, "World T4"),
    "T4-5": LocData(98765594, "World T4"),
    "T4-6": LocData(98765595, "World T4"),
    "T4-7": LocData(98765596, "World T4"),
    "T4-8": LocData(98765597, "World T4"),
    "T4-9": LocData(98765598, "World T4"),
    "T4-10": LocData(98765599, "World T4"),
    "T4-11": LocData(98765600, "World T4"),
    "T4-12": LocData(98765601, "World T4"),

    "T5-1": LocData(98765602, "World T5"),
    "T5-2": LocData(98765603, "World T5"),
    "T5-3": LocData(98765604, "World T5"),
    "T5-4": LocData(98765605, "World T5"),
    "T5-5": LocData(98765606, "World T5"),
}

NeonCosmosWorldsLoc = {
    "T1-X": LocData(98765607, "World T1"),
    "T2-X": LocData(98765608, "World T2"),
    "T3-X": LocData(98765609, "World T3"),
    "T4-X": LocData(98765610, "World T4"),
    "T5-X": LocData(98765611, "World T5"),
}

NeonCosmosWorldsEXTutoLoc = {
    "T1EX-1": LocData(98765612, "World T1EX"),
    "T1EX-2": LocData(98765613, "World T1EX"),
    "T1EX-3": LocData(98765614, "World T1EX"),
    "T1EX-4": LocData(98765615, "World T1EX"),

    "T2EX-1": LocData(98765616, "World T2EX"),
    "T2EX-2": LocData(98765617, "World T2EX"),
    "T2EX-3": LocData(98765618, "World T2EX"),
    "T2EX-4": LocData(98765619, "World T2EX"),

    "T4EX-1": LocData(98765620, "World T4EX"),
    "T4EX-2": LocData(98765621, "World T4EX"),
    "T4EX-3": LocData(98765622, "World T4EX"),
    "T4EX-4": LocData(98765623, "World T4EX"),
}

NeonCosmosWorldsEXLoc = {
    "T1EX-X": LocData(98765624, "World T1EX"),
    "T2EX-X": LocData(98765625, "World T2EX"),
    "T4EX-X": LocData(98765626, "World T4EX"),
    "T3EX-X": LocData(98765627, "World T3EX"),
}

AprilFoolsWorldsLoc = {
    "1J-X": LocData(98765628, "World 1"),
    "2J-X": LocData(98765629, "World 2"),
    "3J-X": LocData(98765630, "World 3"),
    "4J-X": LocData(98765631, "World 4"),
    "5J-X": LocData(98765632, "World 5"),
    "6J-X": LocData(98765633, "World 6"),
    "BJ-X": LocData(98765634, "World B")
}

