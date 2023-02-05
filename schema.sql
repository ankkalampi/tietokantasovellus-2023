DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE npcs (
    id SERIAL PRIMARY KEY,
    name TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE chatrooms (
    id SERIAL PRIMARY KEY,
    name TEXT,
    user_id INTEGER REFERENCES users,
    npc_id INTEGER REFERENCES npcs
);

CREATE TABLE dialogues (
    id SERIAL PRIMARY KEY,
    name TEXT,
    npc_id INTEGER REFERENCES npcs,
    parent_dialogue_id INTEGER REFERENCES dialogues
);

/*  node_types:
        start -> loaded when dialogue is loaded
        middle
        end -> used for saving conversation over status

    content_types:
        utterance -> dialogue line that's played when traversing the node
        condition -> restricts movement along connection if not met
        junction -> removes all connections except for the one chosen
*/
CREATE TABLE nodes (
    id SERIAL PRIMARY KEY,
    node_type INTEGER,
    content_type INTEGER,
    dialogue_id INTEGER REFERENCES dialogues
);

CREATE TABLE connections (
    id SERIAL PRIMARY KEY,
    start_node_id INTEGER REFERENCES nodes,
    end_node_id INTEGER REFERENCES nodes
);

CREATE TABLE utterances (
    id SERIAL PRIMARY KEY,
    player_utterance TEXT,
    npc_utterance TEXT,
    node_id INTEGER REFERENCES nodes
);

