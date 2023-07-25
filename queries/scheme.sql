/* https://vertabelo.com/blog/again-and-again-managing-recurring-events-in-a-data-model/ */
CREATE SCHEMA scheduling AUTHORIZATION admin
    CREATE TABLE recurring_type (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        type VARCHAR(20) NOT NULL
    )
    CREATE TABLE "user" (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        first_name VARCHAR(70),
        second_name VARCHAR(70),
        last_name VARCHAR(70)
    )
    CREATE TABLE event (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        title VARCHAR(50) NOT NULL ,
        event_description VARCHAR(500),
        start_date DATE NOT NULL ,
        end_date DATE,
        start_time TIMESTAMP NOT NULL ,
        end_time TIMESTAMP NOT NULL ,
        is_recurring BOOLEAN NOT NULL ,
        created_by INT REFERENCES scheduling.user (id) ON DELETE RESTRICT NOT NULL ,
        created_date DATE NOT NULL ,
        parent_event_id INT REFERENCES scheduling.event (id) ON DELETE RESTRICT
    )
    CREATE TABLE recurring_pattern (
        event_id INT PRIMARY KEY REFERENCES scheduling.event (id) ON DELETE RESTRICT NOT NULL,
        recurring_type_id INT REFERENCES scheduling.recurring_type (id) ON DELETE RESTRICT NOT NULL,
        separation_count SMALLINT DEFAULT 0,
        day_of_week SMALLINT CHECK ( day_of_week >= 1 AND day_of_week <= 7),
        week_of_month SMALLINT CHECK ( day_of_week >= 1 AND day_of_week <= 4),
        day_of_month SMALLINT CHECK ( day_of_week >= 1 AND day_of_week <= 31),
        month_of_year SMALLINT CHECK ( day_of_week >= 1 AND day_of_week <= 12)
    )
    CREATE TABLE event_instance_exception (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        event_id INT REFERENCES scheduling.event (id) ON DELETE RESTRICT NOT NULL,
        is_rescheduled BOOLEAN NOT NULL ,
        is_cancelled BOOLEAN NOT NULL ,
        start_date DATE NOT NULL ,
        end_date DATE NOT NULL ,
        start_time TIMESTAMP NOT NULL,
        end_time TIMESTAMP NOT NULL ,
        created_by INT REFERENCES scheduling.user (id) ON DELETE RESTRICT NOT NULL,
        created_date DATE NOT NULL
    )
    CREATE TABLE member (
        user_id INT PRIMARY KEY REFERENCES scheduling."user" (id) ON DELETE RESTRICT NOT NULL,
        status VARCHAR(20)
    )
    CREATE TABLE manager (
        user_id INT PRIMARY KEY REFERENCES scheduling."user" (id) ON DELETE RESTRICT NOT NULL
    )
    CREATE TABLE blacklist (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        manager_id INT REFERENCES scheduling.manager (user_id) ON DELETE RESTRICT NOT NULL,
        member_id INT REFERENCES scheduling.member (user_id) ON DELETE RESTRICT NOT NULL
    )
    CREATE TABLE lobby (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        manager INT REFERENCES scheduling.member (user_id) ON DELETE RESTRICT NOT NULL
    )
    CREATE TABLE members_to_lobby (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        lobby_id INT REFERENCES scheduling.lobby (id) ON DELETE RESTRICT NOT NULL,
        member_id INT REFERENCES scheduling.member (user_id) ON DELETE RESTRICT NOT NULL
    )
    CREATE TABLE lobby_join_request (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        lobby_id INT REFERENCES scheduling.lobby (id) ON DELETE RESTRICT NOT NULL,
        member_id INT REFERENCES scheduling.member (user_id) ON DELETE RESTRICT NOT NULL,
        UNIQUE (lobby_id, member_id)
    )
    CREATE TABLE attend_event_request (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        event_id INT REFERENCES scheduling.event (id) ON DELETE RESTRICT NOT NULL,
        member_id INT REFERENCES scheduling.member (user_id) ON DELETE RESTRICT NOT NULL,
        is_pending BOOLEAN NOT NULL DEFAULT TRUE,
        description VARCHAR(150),
        is_cancelled BOOLEAN NOT NULL DEFAULT FALSE,
        UNIQUE (event_id, member_id)
    )
