#TABLE
CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


#Task

CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    project_id INTEGER NOT NULL,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    duration INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_task_project
        FOREIGN KEY (project_id)
        REFERENCES project(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_task_duration_positive
        CHECK (duration > 0)
);
# this index is created to optimize queries that filter tasks by their associated project_id

CREATE INDEX idx_task_project_id ON task(project_id);


# created to represent the relationships between tasks, where one task (predecessor) must be completed
# before another task (successor) can start. The table includes foreign key constraints to ensure
# referential integrity and a check constraint to prevent self-dependencies. Additionally, unique
# constraints and indexes are added to optimize query performance when retrieving dependencies based
# on predecessor or successor tasks.
#Dependency

CREATE TABLE dependency (
    id SERIAL PRIMARY KEY,
    predecessor_id INTEGER NOT NULL,
    successor_id INTEGER NOT NULL,

    CONSTRAINT fk_dependency_predecessor
        FOREIGN KEY (predecessor_id)
        REFERENCES task(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_dependency_successor
        FOREIGN KEY (successor_id)
        REFERENCES task(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_no_self_dependency
        CHECK (predecessor_id <> successor_id),

    CONSTRAINT uq_dependency_unique
        UNIQUE (predecessor_id, successor_id)
);


CREATE INDEX idx_dependency_predecessor ON dependency(predecessor_id);
CREATE INDEX idx_dependency_successor ON dependency(successor_id);



#Calculation_result

CREATE TABLE calculation_result (
    id SERIAL PRIMARY KEY,
    task_id INTEGER NOT NULL UNIQUE,
    early_start INTEGER NOT NULL,
    early_finish INTEGER NOT NULL,
    late_start INTEGER NOT NULL,
    late_finish INTEGER NOT NULL,
    slack INTEGER NOT NULL,
    is_critical BOOLEAN NOT NULL,
    calculated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_calculation_task
        FOREIGN KEY (task_id)
        REFERENCES task(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_times_non_negative
        CHECK (
            early_start >= 0 AND
            early_finish >= 0 AND
            late_start >= 0 AND
            late_finish >= 0 AND
            slack >= 0
        )
);

#THIS SCHEMA DEFINES THE STRUCTURE OF THE DATABASE FOR A PROJECT MANAGEMENT APPLICATION. IT INCLUDES TABLES FOR PROJECTS
#TASKS, DEPENDENCIES BETWEEN TASKS, AND CALCULATION RESULTS FOR CRITICAL PATH ANALYSIS. EACH TABLE HAS APPROPRIATE CONSTRAINTS
#TO ENSURE DATA INTEGRITY AND RELATIONSHIPS BETWEEN TABLES. 
