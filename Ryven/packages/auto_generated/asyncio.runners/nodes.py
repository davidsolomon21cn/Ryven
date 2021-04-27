
from NENV import *

import asyncio.runners


class NodeBase(Node):
    pass


class _All_Tasks_Compat_Node(NodeBase):
    title = '_all_tasks_compat'
    type_ = 'asyncio.runners'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='loop', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._all_tasks_compat(self.input(0)))
        

class _Enter_Task_Node(NodeBase):
    title = '_enter_task'
    type_ = 'asyncio.runners'
    doc = """Enter into task execution or resume suspended task.

Task belongs to loop.

Returns None."""
    init_inputs = [
        NodeInputBP(label='loop'),
        NodeInputBP(label='task'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._enter_task(self.input(0), self.input(1)))
        

class _Get_Running_Loop_Node(NodeBase):
    title = '_get_running_loop'
    type_ = 'asyncio.runners'
    doc = """Return the running event loop or None.

This is a low-level function intended to be used by event loops.
This function is thread-specific."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._get_running_loop())
        

class _Leave_Task_Node(NodeBase):
    title = '_leave_task'
    type_ = 'asyncio.runners'
    doc = """Leave task execution or suspend a task.

Task belongs to loop.

Returns None."""
    init_inputs = [
        NodeInputBP(label='loop'),
        NodeInputBP(label='task'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._leave_task(self.input(0), self.input(1)))
        

class _Register_Task_Node(NodeBase):
    title = '_register_task'
    type_ = 'asyncio.runners'
    doc = """Register a new task in asyncio as executed by loop.

Returns None."""
    init_inputs = [
        NodeInputBP(label='task'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._register_task(self.input(0)))
        

class _Set_Running_Loop_Node(NodeBase):
    title = '_set_running_loop'
    type_ = 'asyncio.runners'
    doc = """Set the running event loop.

This is a low-level function intended to be used by event loops.
This function is thread-specific."""
    init_inputs = [
        NodeInputBP(label='loop'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._set_running_loop(self.input(0)))
        

class _Unregister_Task_Node(NodeBase):
    title = '_unregister_task'
    type_ = 'asyncio.runners'
    doc = """Unregister a task.

Returns None."""
    init_inputs = [
        NodeInputBP(label='task'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners._unregister_task(self.input(0)))
        

class All_Tasks_Node(NodeBase):
    title = 'all_tasks'
    type_ = 'asyncio.runners'
    doc = """Return a set of all tasks for the loop."""
    init_inputs = [
        NodeInputBP(label='loop', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.all_tasks(self.input(0)))
        

class As_Completed_Node(NodeBase):
    title = 'as_completed'
    type_ = 'asyncio.runners'
    doc = """Return an iterator whose values are coroutines.

    When waiting for the yielded coroutines you'll get the results (or
    exceptions!) of the original Futures (or coroutines), in the order
    in which and as soon as they complete.

    This differs from PEP 3148; the proper way to use this is:

        for f in as_completed(fs):
            result = await f  # The 'await' may raise.
            # Use result.

    If a timeout is specified, the 'await' will raise
    TimeoutError when the timeout occurs before all Futures are done.

    Note: The futures 'f' are not necessarily members of fs.
    """
    init_inputs = [
        NodeInputBP(label='fs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.as_completed(self.input(0)))
        

class Coroutine_Node(NodeBase):
    title = 'coroutine'
    type_ = 'asyncio.runners'
    doc = """Decorator to mark coroutines.

    If the coroutine is not yielded from before it is destroyed,
    an error message is logged.
    """
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.coroutine(self.input(0)))
        

class Create_Subprocess_Exec_Node(NodeBase):
    title = 'create_subprocess_exec'
    type_ = 'asyncio.runners'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='program'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.create_subprocess_exec(self.input(0)))
        

class Create_Subprocess_Shell_Node(NodeBase):
    title = 'create_subprocess_shell'
    type_ = 'asyncio.runners'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='cmd'),
        NodeInputBP(label='stdin', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stdout', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stderr', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='loop', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=65536, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.create_subprocess_shell(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Create_Task_Node(NodeBase):
    title = 'create_task'
    type_ = 'asyncio.runners'
    doc = """Schedule the execution of a coroutine object in a spawn task.

    Return a Task object.
    """
    init_inputs = [
        NodeInputBP(label='coro'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.create_task(self.input(0)))
        

class Current_Task_Node(NodeBase):
    title = 'current_task'
    type_ = 'asyncio.runners'
    doc = """Return a currently executed task."""
    init_inputs = [
        NodeInputBP(label='loop', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.current_task(self.input(0)))
        

class Ensure_Future_Node(NodeBase):
    title = 'ensure_future'
    type_ = 'asyncio.runners'
    doc = """Wrap a coroutine or an awaitable in a future.

    If the argument is a Future, it is returned directly.
    """
    init_inputs = [
        NodeInputBP(label='coro_or_future'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.ensure_future(self.input(0)))
        

class Gather_Node(NodeBase):
    title = 'gather'
    type_ = 'asyncio.runners'
    doc = """Return a future aggregating results from the given coroutines/futures.

    Coroutines will be wrapped in a future and scheduled in the event
    loop. They will not necessarily be scheduled in the same order as
    passed in.

    All futures must share the same event loop.  If all the tasks are
    done successfully, the returned future's result is the list of
    results (in the order of the original sequence, not necessarily
    the order of results arrival).  If *return_exceptions* is True,
    exceptions in the tasks are treated the same as successful
    results, and gathered in the result list; otherwise, the first
    raised exception will be immediately propagated to the returned
    future.

    Cancellation: if the outer Future is cancelled, all children (that
    have not completed yet) are also cancelled.  If any child is
    cancelled, this is treated as if it raised CancelledError --
    the outer Future is *not* cancelled in this case.  (This is to
    prevent the cancellation of one child to cause other children to
    be cancelled.)

    If *return_exceptions* is False, cancelling gather() after it
    has been marked done won't cancel any submitted awaitables.
    For instance, gather can be marked done after propagating an
    exception to the caller, therefore, calling ``gather.cancel()``
    after catching an exception (raised by one of the awaitables) from
    gather won't cancel any other awaitables.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.gather())
        

class Get_Child_Watcher_Node(NodeBase):
    title = 'get_child_watcher'
    type_ = 'asyncio.runners'
    doc = """Equivalent to calling get_event_loop_policy().get_child_watcher()."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.get_child_watcher())
        

class Get_Event_Loop_Node(NodeBase):
    title = 'get_event_loop'
    type_ = 'asyncio.runners'
    doc = """Return an asyncio event loop.

When called from a coroutine or a callback (e.g. scheduled with
call_soon or similar API), this function will always return the
running event loop.

If there is no running event loop set, the function will return
the result of `get_event_loop_policy().get_event_loop()` call."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.get_event_loop())
        

class Get_Event_Loop_Policy_Node(NodeBase):
    title = 'get_event_loop_policy'
    type_ = 'asyncio.runners'
    doc = """Get the current event loop policy."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.get_event_loop_policy())
        

class Get_Running_Loop_Node(NodeBase):
    title = 'get_running_loop'
    type_ = 'asyncio.runners'
    doc = """Return the running event loop.  Raise a RuntimeError if there is none.

This function is thread-specific."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.get_running_loop())
        

class Iscoroutine_Node(NodeBase):
    title = 'iscoroutine'
    type_ = 'asyncio.runners'
    doc = """Return True if obj is a coroutine object."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.iscoroutine(self.input(0)))
        

class Iscoroutinefunction_Node(NodeBase):
    title = 'iscoroutinefunction'
    type_ = 'asyncio.runners'
    doc = """Return True if func is a decorated coroutine function."""
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.iscoroutinefunction(self.input(0)))
        

class Isfuture_Node(NodeBase):
    title = 'isfuture'
    type_ = 'asyncio.runners'
    doc = """Check for a Future.

    This returns True when obj is a Future instance or is advertising
    itself as duck-type compatible by setting _asyncio_future_blocking.
    See comment in Future for more details.
    """
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.isfuture(self.input(0)))
        

class New_Event_Loop_Node(NodeBase):
    title = 'new_event_loop'
    type_ = 'asyncio.runners'
    doc = """Equivalent to calling get_event_loop_policy().new_event_loop()."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.new_event_loop())
        

class Open_Connection_Node(NodeBase):
    title = 'open_connection'
    type_ = 'asyncio.runners'
    doc = """A wrapper for create_connection() returning a (reader, writer) pair.

    The reader returned is a StreamReader instance; the writer is a
    StreamWriter instance.

    The arguments are all the usual arguments to create_connection()
    except protocol_factory; most common are positional host and port,
    with various optional keyword arguments following.

    Additional optional keyword arguments are loop (to set the event loop
    instance to use) and limit (to set the buffer limit passed to the
    StreamReader).

    (If you want to customize the StreamReader and/or
    StreamReaderProtocol classes, just copy the code -- there's
    really nothing special here except some convenience.)
    """
    init_inputs = [
        NodeInputBP(label='host', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='port', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.open_connection(self.input(0), self.input(1)))
        

class Run_Node(NodeBase):
    title = 'run'
    type_ = 'asyncio.runners'
    doc = """Execute the coroutine and return the result.

    This function runs the passed coroutine, taking care of
    managing the asyncio event loop and finalizing asynchronous
    generators.

    This function cannot be called when another asyncio event loop is
    running in the same thread.

    If debug is True, the event loop will be run in debug mode.

    This function always creates a new event loop and closes it at the end.
    It should be used as a main entry point for asyncio programs, and should
    ideally only be called once.

    Example:

        async def main():
            await asyncio.sleep(1)
            print('hello')

        asyncio.run(main())
    """
    init_inputs = [
        NodeInputBP(label='main'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.run(self.input(0)))
        

class Run_Coroutine_Threadsafe_Node(NodeBase):
    title = 'run_coroutine_threadsafe'
    type_ = 'asyncio.runners'
    doc = """Submit a coroutine object to a given event loop.

    Return a concurrent.futures.Future to access the result.
    """
    init_inputs = [
        NodeInputBP(label='coro'),
        NodeInputBP(label='loop'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.run_coroutine_threadsafe(self.input(0), self.input(1)))
        

class Set_Child_Watcher_Node(NodeBase):
    title = 'set_child_watcher'
    type_ = 'asyncio.runners'
    doc = """Equivalent to calling
    get_event_loop_policy().set_child_watcher(watcher)."""
    init_inputs = [
        NodeInputBP(label='watcher'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.set_child_watcher(self.input(0)))
        

class Set_Event_Loop_Node(NodeBase):
    title = 'set_event_loop'
    type_ = 'asyncio.runners'
    doc = """Equivalent to calling get_event_loop_policy().set_event_loop(loop)."""
    init_inputs = [
        NodeInputBP(label='loop'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.set_event_loop(self.input(0)))
        

class Set_Event_Loop_Policy_Node(NodeBase):
    title = 'set_event_loop_policy'
    type_ = 'asyncio.runners'
    doc = """Set the current event loop policy.

    If policy is None, the default policy is restored."""
    init_inputs = [
        NodeInputBP(label='policy'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.set_event_loop_policy(self.input(0)))
        

class Shield_Node(NodeBase):
    title = 'shield'
    type_ = 'asyncio.runners'
    doc = """Wait for a future, shielding it from cancellation.

    The statement

        res = await shield(something())

    is exactly equivalent to the statement

        res = await something()

    *except* that if the coroutine containing it is cancelled, the
    task running in something() is not cancelled.  From the POV of
    something(), the cancellation did not happen.  But its caller is
    still cancelled, so the yield-from expression still raises
    CancelledError.  Note: If something() is cancelled by other means
    this will still cancel shield().

    If you want to completely ignore cancellation (not recommended)
    you can combine shield() with a try/except clause, as follows:

        try:
            res = await shield(something())
        except CancelledError:
            res = None
    """
    init_inputs = [
        NodeInputBP(label='arg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.shield(self.input(0)))
        

class Sleep_Node(NodeBase):
    title = 'sleep'
    type_ = 'asyncio.runners'
    doc = """Coroutine that completes after a given time (in seconds)."""
    init_inputs = [
        NodeInputBP(label='delay'),
        NodeInputBP(label='result', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.sleep(self.input(0), self.input(1)))
        

class Start_Server_Node(NodeBase):
    title = 'start_server'
    type_ = 'asyncio.runners'
    doc = """Start a socket server, call back for each client connected.

    The first parameter, `client_connected_cb`, takes two parameters:
    client_reader, client_writer.  client_reader is a StreamReader
    object, while client_writer is a StreamWriter object.  This
    parameter can either be a plain callback function or a coroutine;
    if it is a coroutine, it will be automatically converted into a
    Task.

    The rest of the arguments are all the usual arguments to
    loop.create_server() except protocol_factory; most common are
    positional host and port, with various optional keyword arguments
    following.  The return value is the same as loop.create_server().

    Additional optional keyword arguments are loop (to set the event loop
    instance to use) and limit (to set the buffer limit passed to the
    StreamReader).

    The return value is the same as loop.create_server(), i.e. a
    Server object which can be used to stop the service.
    """
    init_inputs = [
        NodeInputBP(label='client_connected_cb'),
        NodeInputBP(label='host', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='port', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.start_server(self.input(0), self.input(1), self.input(2)))
        

class Wait_Node(NodeBase):
    title = 'wait'
    type_ = 'asyncio.runners'
    doc = """Wait for the Futures and coroutines given by fs to complete.

    The fs iterable must not be empty.

    Coroutines will be wrapped in Tasks.

    Returns two sets of Future: (done, pending).

    Usage:

        done, pending = await asyncio.wait(fs)

    Note: This does not raise TimeoutError! Futures that aren't done
    when the timeout occurs are returned in the second set.
    """
    init_inputs = [
        NodeInputBP(label='fs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.wait(self.input(0)))
        

class Wait_For_Node(NodeBase):
    title = 'wait_for'
    type_ = 'asyncio.runners'
    doc = """Wait for the single Future or coroutine to complete, with timeout.

    Coroutine will be wrapped in Task.

    Returns result of the Future or coroutine.  When a timeout occurs,
    it cancels the task and raises TimeoutError.  To avoid the task
    cancellation, wrap it in shield().

    If the wait is cancelled, the task is also cancelled.

    This function is a coroutine.
    """
    init_inputs = [
        NodeInputBP(label='fut'),
        NodeInputBP(label='timeout'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.wait_for(self.input(0), self.input(1)))
        

class Wrap_Future_Node(NodeBase):
    title = 'wrap_future'
    type_ = 'asyncio.runners'
    doc = """Wrap concurrent.futures.Future object."""
    init_inputs = [
        NodeInputBP(label='future'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.runners.wrap_future(self.input(0)))
        


export_nodes(
    _All_Tasks_Compat_Node,
    _Enter_Task_Node,
    _Get_Running_Loop_Node,
    _Leave_Task_Node,
    _Register_Task_Node,
    _Set_Running_Loop_Node,
    _Unregister_Task_Node,
    All_Tasks_Node,
    As_Completed_Node,
    Coroutine_Node,
    Create_Subprocess_Exec_Node,
    Create_Subprocess_Shell_Node,
    Create_Task_Node,
    Current_Task_Node,
    Ensure_Future_Node,
    Gather_Node,
    Get_Child_Watcher_Node,
    Get_Event_Loop_Node,
    Get_Event_Loop_Policy_Node,
    Get_Running_Loop_Node,
    Iscoroutine_Node,
    Iscoroutinefunction_Node,
    Isfuture_Node,
    New_Event_Loop_Node,
    Open_Connection_Node,
    Run_Node,
    Run_Coroutine_Threadsafe_Node,
    Set_Child_Watcher_Node,
    Set_Event_Loop_Node,
    Set_Event_Loop_Policy_Node,
    Shield_Node,
    Sleep_Node,
    Start_Server_Node,
    Wait_Node,
    Wait_For_Node,
    Wrap_Future_Node,
)